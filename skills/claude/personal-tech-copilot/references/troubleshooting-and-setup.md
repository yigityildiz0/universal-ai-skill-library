# Troubleshooting and setup playbook

## Evidence hierarchy

1. Exact error, screenshot, log, and observed behavior on the user's device
2. Current official support/manual/compatibility documentation for the exact model and version
3. Release notes, status pages, and vendor advisories
4. Reproducible reports for the same version/hardware combination
5. General community advice, clearly labeled and used only after safer evidence

## Isolation matrix

Change one axis at a time:

- hardware versus software;
- one device versus every device;
- one account versus every account;
- local network versus another trusted network;
- wired versus wireless;
- app versus browser/system feature;
- current user profile versus a temporary clean profile;
- accessory/cable/adapter versus a known-good equivalent;
- setting versus service outage or unsupported feature.

Record the result that would confirm or reject each hypothesis. Avoid reinstall/reset until isolation shows it is relevant.

## Action ladder

1. Verify identity, power, storage, time/date, permissions, connection, and service status.
2. Reproduce and capture the exact error.
3. Restart only the affected layer.
4. Test a safe known-good alternative.
5. Update using official stable channels when the release is relevant and rollback is understood.
6. Repair configuration or pairing with a documented undo path.
7. Reinstall or reset the narrow component after backup.
8. Use factory reset, partition/registry changes, firmware recovery, or hardware service only with explicit need and recovery readiness.

## Cross-ecosystem checks

For Apple/Huawei/Windows or smart-home interactions, verify:

- supported protocol and version, not just brand marketing;
- account/region requirements;
- hub, bridge, cloud, or same-network dependency;
- Wi-Fi band, Bluetooth, Thread, Matter, HomeKit, casting, or vendor-specific limits;
- feature loss when using a non-native ecosystem;
- notification/background/battery restrictions;
- ownership transfer, reset, and resale procedure.

## App recommendation checks

For scanning, PDF, backup, remote-access, utility, or productivity apps, verify:

- current official Play Store, App Store, Microsoft Store, or publisher listing;
- exact OS/version and country availability;
- whether core use, saving, sharing, and export are actually free;
- page/file limits, watermark, OCR quality, resolution, ads, sign-in, cloud-only
  processing, subscription trial, and cancellation terms;
- permissions, data retention, analytics, uploads, encryption, and whether a
  local/offline alternative exists;
- recent maintenance and repeated same-version failure patterns.

Rank apps by the user's real completion path, not download count or a marketing
feature list.

## Peripheral remapping checks

For a mouse, keyboard, controller, macro pad, or similar accessory, identify the
exact model/revision and check official configuration software, supported
operating systems, remappable versus fixed buttons, onboard memory, per-app
profiles, macros, firmware, and administrator requirements. Distinguish a
temporary software mapping from a mapping stored on the device.

## Remote access minimum

Document host/client devices, network direction, authentication, encryption, permissions, wake/lock behavior, unattended-access setting, file/clipboard transfer, session logging, and recovery. Never recommend exposing RDP/VNC or an admin panel directly to the public internet without a securely designed gateway/VPN and a clear reason.

## Handoff bundle

If unresolved, collect only: exact models and versions, error text, steps to reproduce, changes tried with results, relevant sanitized screenshots/logs, and whether the problem follows device/account/network. Remove usernames, emails, serials, IPs, tokens, and unrelated personal data.
