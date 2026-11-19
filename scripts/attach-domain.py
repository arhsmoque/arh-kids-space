"""Attach kids.arh-urus.com to the arh-kids-space Worker (Workers custom domain).

wrangler 4 uploads the Worker but then fails on GET /workers/workers/<name> (code 10007) before
it applies `routes`, so the custom domain is attached here instead. Idempotent.

  g4-secrets-cli inject --env CLOUDFLARE_API_TOKEN=arh-cloudflare-workers-local/api_token -- python scripts/attach-domain.py
"""
import json
import os
import urllib.error
import urllib.request

ACCOUNT, ZONE_NAME, HOST, SERVICE = "dc3bfa957bdf216b7cc45214455aaa72", "arh-urus.com", "kids.arh-urus.com", "arh-kids-space"
API = "https://api.cloudflare.com/client/v4"


def cf(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"Bearer {os.environ['CLOUDFLARE_API_TOKEN']}",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)["result"]
    except urllib.error.HTTPError as e:
        raise SystemExit(f"cloudflare {method} {path}: {e.code} {e.read().decode(errors='replace')[:400]}") from None


zone = cf("GET", f"/zones?name={ZONE_NAME}")[0]["id"]
script = cf("GET", f"/accounts/{ACCOUNT}/workers/scripts/{SERVICE}/settings")
print("worker exists:", SERVICE, "| compatibility_date", script.get("compatibility_date"))
have = [d for d in cf("GET", f"/accounts/{ACCOUNT}/workers/domains?hostname={HOST}") if d["hostname"] == HOST]
if have and have[0]["service"] == SERVICE:
    print("domain already attached:", HOST)
else:
    d = cf("PUT", f"/accounts/{ACCOUNT}/workers/domains",
           {"hostname": HOST, "service": SERVICE, "zone_id": zone, "environment": "production"})
    print("attached:", d["hostname"], "->", d["service"])
