title: Fix Plesk installer download failures with HTTPS
date: October 24th, 2026
slug: fix-plesk-installer-download-failures-with-https
category: Plesk + Linux + Troubleshooting + DevOps
status: active

While updating Plesk on an Ubuntu server, I came across an error that didn't make much sense for an existing installation:

```text
ERROR: No products are installed yet.
Use the 'install' command to install one first.
```

The installer logs gave me a more useful clue:

```text
Can't process versions.inf3:
Failed to download the file http://autoinstall.plesk.com/versions.inf3
```

The installer was trying to download its repository metadata over HTTP. I checked whether the HTTPS endpoint was reachable from the same server:

```bash
curl -ILv --connect-timeout 10 --max-time 20 https://autoinstall.plesk.com/versions.inf3
```

Here, `-I` requests response headers, `-L` follows redirects, and `-v` shows connection details. The timeouts keep the check from hanging indefinitely.

HTTPS was reachable. That suggested a problem with the HTTP request path, although it didn't establish whether a firewall, proxy, or another network condition was responsible.

I then ran the installer as root with an explicit HTTPS package source:

```bash
plesk installer \
  --source https://autoinstall.plesk.com \
  --select-release-latest \
  --upgrade-installed-components
```

The `--source` option overrides the package source for this run, as described in the [Plesk installer documentation](https://docs.plesk.com/en-US/onyx/deployment-guide/plesk-installation-and-upgrade-on-multiple-servers/installing-plesk-in-unattended-mode/installing-plesk-for-linux-in-unattended-mode.76510/). The remaining options select the latest release and update installed components; see the [Plesk update documentation](https://doc.plesk.com/en-US/obsidian/administrator-guide/plesk-updates-and-upgrades.59215/).

This command performs an update, so run it during your planned maintenance window with a current backup. In a multiline shell command, each backslash must be the final character on its line.

Using HTTPS got the installer past the metadata download failure. If you see the same initial error, check the installer logs first—the failed download was the clue that mattered here.

Hope you found this useful!
