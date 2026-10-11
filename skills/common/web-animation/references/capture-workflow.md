# Seek and compare animation frames

Use the active host's actual browser/DevTools/Playwright tools. Inspect their catalog rather than invoking upstream tool-name placeholders. This workflow needs no bundled shell scripts or extra packages.

1. Use the project's existing preview and test harness. Add a development-only `?t=<seconds>` input only when animation testing is part of the requested implementation. A query parameter alone does not freeze an animation: wire it to the paused timeline, WAAPI `currentTime`, Lottie frame or deterministic render function.
2. Open the same explicit page/tab at representative times (for example 0, 1.5 and 3 seconds). Wait for fonts/assets and harness readiness. Compare captures at the same viewport and scale.
3. Test live playback separately. Stills cannot establish frame rate, dropped frames, focus handling or reduced-motion behavior. Check keyboard operation, final visible content and emulated `prefers-reduced-motion: reduce` with available tools.
4. If a contact sheet is requested, combine authorized captures with already-available image tools and label timestamps. Otherwise compare frames directly; do not generate an unsolicited downloadable image/PDF.
5. If browser access or a harness is unavailable, report static review and unverified behaviors. Never claim runtime performance or visual approval from source inspection alone.
