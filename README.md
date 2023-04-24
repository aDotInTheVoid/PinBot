# PinBot

A Discord Bot, to allow users to pin messages, without giving them manage message perms.

## Quickstart

1. Go to <https://discord.com/developers/applications>
2. Click "New Application"
3. Click "Add Bot" 
4. Copy the token.
5. Put it in `.env`
6. Goto "OAuth2 URL Generator"
7. Select "Bot", "Send Messages", "Mannage Messages" and "Use slash commands"
8. Goto the url
9. Add it to your server.

## Run locally with docker/podman

```
podman build . -t pinbot
podman run --env-file ./.env pinbot
```

