# DirectAdmin DNS Automation Research

## Summary
DirectAdmin's Evolution UI still supports legacy API (`CMD_API_DNS_*`) which returns JSON.

## Solution

### Step 1: Create Login Key
You need to manually create a Login Key in DirectAdmin with DNS permissions:
- Go to DirectAdmin → Login Keys → Create New
- Enable: CMD_API_DNS_ADMIN
- Restrict to VPS IP

### Step 2: Use API
```bash
# Add A record
curl -s -k 'https://admin:API_KEY@dahost6.vpslocal.co.za:2222/CMD_API_DNS' \
  -d 'action=add' \
  -d 'domain=interlinkedcapital.co.za' \
  -d 'type=A' \
  -d 'name=@' \
  -d 'value=76.38.136.163'

# Add CNAME  
curl -s -k 'https://admin:API_KEY@dahost6.vpslocal.co.za:2222/CMD_API_DNS' \
  -d 'action=add' \
  -d 'domain=interlinkedcapital.co.za' \
  -d 'type=CNAME' \
  -d 'name=www' \
  -d 'value=cname.vercel-dns.com'
```

## Next Steps
1. Create login key in DirectAdmin (manual)
2. Save API key to vault
3. Test API calls
4. Automate with Python script

---
_Date: 2026-03-07_
