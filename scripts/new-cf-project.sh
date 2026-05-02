#!/usr/bin/env bash
# Usage: ./scripts/new-cf-project.sh <github-repo> [<cf-project-name>] [<deploy-dir>]
#
# Example:
#   ./scripts/new-cf-project.sh beelalcoffee beelalcoffee dist
#   ./scripts/new-cf-project.sh my-new-site                     # defaults: same name, dir="."
#
# Prerequisites:
#   - gh CLI installed and authenticated (gh auth login)
#   - wrangler installed: npm i -g wrangler
#   - CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID set in env,
#     OR stored in ~/.cf-credentials (sourced below)
#
# What it does:
#   1. Creates the Cloudflare Pages project (if not exists)
#   2. Adds CF secrets to the GitHub repo
#   3. Adds a minimal deploy workflow that calls the reusable workflow in arh-kids-space

set -euo pipefail

GITHUB_OWNER="arhsmoque"
REUSABLE_WORKFLOW="arhsmoque/arh-kids-space/.github/workflows/reusable-cf-pages-deploy.yml@main"
CF_CREDS_FILE="$HOME/.cf-credentials"

GITHUB_REPO="${1:?Usage: $0 <github-repo> [<cf-project-name>] [<deploy-dir>]}"
CF_PROJECT="${2:-$GITHUB_REPO}"
DEPLOY_DIR="${3:-.}"

# ── Load credentials ──────────────────────────────────────────────────────────
if [[ -z "${CLOUDFLARE_API_TOKEN:-}" && -f "$CF_CREDS_FILE" ]]; then
  # shellcheck source=/dev/null
  source "$CF_CREDS_FILE"
fi
: "${CLOUDFLARE_API_TOKEN:?Set CLOUDFLARE_API_TOKEN or add it to $CF_CREDS_FILE}"
: "${CLOUDFLARE_ACCOUNT_ID:?Set CLOUDFLARE_ACCOUNT_ID or add it to $CF_CREDS_FILE}"

echo "→ Repo:       $GITHUB_OWNER/$GITHUB_REPO"
echo "→ CF project: $CF_PROJECT"
echo "→ Deploy dir: $DEPLOY_DIR"
echo ""

# ── 1. Create Cloudflare Pages project ───────────────────────────────────────
echo "[1/3] Creating Cloudflare Pages project '$CF_PROJECT'..."
CLOUDFLARE_API_TOKEN=$CLOUDFLARE_API_TOKEN \
CLOUDFLARE_ACCOUNT_ID=$CLOUDFLARE_ACCOUNT_ID \
  npx wrangler pages project create "$CF_PROJECT" --production-branch main 2>&1 \
  | grep -v "^$" || true   # ignore "already exists" errors

# ── 2. Add secrets to GitHub repo ────────────────────────────────────────────
echo "[2/3] Adding Cloudflare secrets to GitHub repo..."
gh secret set CLOUDFLARE_API_TOKEN \
  --repo "$GITHUB_OWNER/$GITHUB_REPO" \
  --body "$CLOUDFLARE_API_TOKEN"

gh secret set CLOUDFLARE_ACCOUNT_ID \
  --repo "$GITHUB_OWNER/$GITHUB_REPO" \
  --body "$CLOUDFLARE_ACCOUNT_ID"

# ── 3. Add deploy workflow to repo ───────────────────────────────────────────
echo "[3/3] Adding deploy workflow to $GITHUB_OWNER/$GITHUB_REPO..."
WORKFLOW_CONTENT=$(cat <<YAML
name: Deploy to Cloudflare Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    uses: $REUSABLE_WORKFLOW
    with:
      project-name: $CF_PROJECT
      directory: $DEPLOY_DIR
    secrets: inherit
YAML
)

# Create or update the workflow file via GitHub API
ENCODED=$(echo "$WORKFLOW_CONTENT" | base64 -w0)
EXISTING_SHA=$(gh api "repos/$GITHUB_OWNER/$GITHUB_REPO/contents/.github/workflows/deploy-cf-pages.yml" \
  --jq '.sha' 2>/dev/null || true)

if [[ -n "$EXISTING_SHA" ]]; then
  gh api "repos/$GITHUB_OWNER/$GITHUB_REPO/contents/.github/workflows/deploy-cf-pages.yml" \
    --method PUT \
    --field message="ci: update Cloudflare Pages deploy workflow" \
    --field content="$ENCODED" \
    --field sha="$EXISTING_SHA" \
    --silent
else
  gh api "repos/$GITHUB_OWNER/$GITHUB_REPO/contents/.github/workflows/deploy-cf-pages.yml" \
    --method PUT \
    --field message="ci: add Cloudflare Pages auto-deploy" \
    --field content="$ENCODED" \
    --silent
fi

echo ""
echo "✓ Done! $CF_PROJECT will auto-deploy to:"
echo "  https://$CF_PROJECT.pages.dev"
echo ""
echo "Next push to main on $GITHUB_OWNER/$GITHUB_REPO will trigger a deploy."
