# Browser Debugging Playbooks

Use only the section that matches the observed failure. Preserve the existing test contract and do not install tools just to follow a playbook.

## UI and interaction

Capture the initial state, intended action, visible result, focus movement, DOM/accessible name, and the smallest reproducible viewport/state. Test keyboard and touch equivalents for pointer-driven flows. Check loading, empty, error, permission, long-content, and reduced-motion states when they exist.

## Network and API

Record request method, status, timing, cache behavior, payload shape, response category, and the visible user effect. Redact headers, cookies, IDs, and secrets. Compare a failed request with a known-good request only when they share authorized fixtures and environment.

## Performance

Capture the route, device/viewport, cache state, network profile, trace method, and repetition count. Check user-visible loading, long tasks, layout shifts, interaction delay, image/font loading, and unnecessary third-party work. Treat lab traces and real-user metrics as different evidence types.

## Accessibility

Check semantic landmarks, heading order, accessible names, focus order/visibility, keyboard traps, form errors, dynamic announcements, contrast, zoom/reflow, and reduced motion. Automation is a finding aid, not proof.

## After a fix

Replay the exact failing path, then run the smallest nearby-regression matrix. Capture what changed, what was retested, and what remains untested.
