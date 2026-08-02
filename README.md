<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-sigma-five.vercel.app/api?username=casablanque-code&show_icons=true&theme=dracula">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats-sigma-five.vercel.app/api?username=casablanque-code&show_icons=true&theme=default">
  <img alt="GitHub Stats" src="https://github-readme-stats-sigma-five.vercel.app/api?username=casablanque-code&show_icons=true&theme=dracula">
</picture>

### Open Source

#### 🔵 Go
* **[cfzt](https://github.com/casablanque-code/cfzt)** (`zt`) — Zero Trust tunnel manager that exposes local services through Cloudflare, manages system daemons and access policies, and handles UDP/QUIC fallback recovery.  
[![Go Reference](https://badgen.net/badge/go.dev/reference/1d4e89?icon=go)](https://pkg.go.dev/github.com/casablanque-code/cfzt)
[![Gitleaks](https://badgen.net/badge/gitleaks/protected/284b63?icon=github)](https://github.com/casablanque-code/cfzt/actions/workflows/gitleaks.yml)
[![codecov](https://codecov.io/gh/casablanque-code/cfzt/branch/main/graph/badge.svg)](https://codecov.io/gh/casablanque-code/cfzt)
[![Tiny Tool Town](https://badgen.net/badge/featured/TinyToolTown/1d4e89)](https://www.tinytooltown.com/tools/cfzt/)
[![Release](https://badgen.net/github/release/casablanque-code/cfzt?color=1b6838)](https://github.com/casablanque-code/cfzt/releases/latest)

#### ⚪ C
* **[khm](https://github.com/casablanque-code/khm)** — Known Hosts Manager. A zero-dependency CLI tool to audit, diff, and scan SSH `known_hosts` using raw BSD sockets and a partial SSH handshake.  
[![Zero Dependencies](https://badgen.net/badge/dependencies/zero/1b6838)](https://github.com/casablanque-code/khm#readme)
[![Platform](https://badgen.net/badge/platform/Linux/343a40)](https://github.com/casablanque-code/khm#readme)
[![GitHub release](https://badgen.net/github/release/casablanque-code/khm?color=1b6838)](https://github.com/casablanque-code/khm/releases/latest)
[![GitHub All Releases](https://img.shields.io/github/downloads/casablanque-code/khm/total?color=284b63&style=flat)](https://github.com/casablanque-code/khm/releases)

#### 🦀 Rust
* **[ios-config](https://crates.io/crates/ios-config)** — Parser and high-level wrapper for Cisco IOS configurations.  
[![Crates.io Version](https://badgen.net/crates/v/ios-config?color=e08b6c&icon=crates)](https://crates.io/crates/ios-config)
[![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/ios-config/latest/ios_config/)
[![Crates.io Downloads](https://badgen.net/crates/d/ios-config?color=284b63)](https://crates.io/crates/ios-config)

* **[netconv-core](https://crates.io/crates/netconv-core)** — Vendor-agnostic IR (intermediate representation) types and traits for network device configuration conversion. Used by ios-config and the netconv renderers.  
[![Crates.io Version](https://badgen.net/crates/v/netconv-core?color=e08b6c&icon=crates)](https://crates.io/crates/netconv-core)
[![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/netconv-core/latest/netconv_core/)
[![Crates.io Downloads](https://badgen.net/crates/d/netconv-core?color=284b63)](https://crates.io/crates/netconv-core)

* **[gai-inspector](https://crates.io/crates/gai-inspector)** (`gai`) — getaddrinfo inspector: explains how a name turns into an IP (nsswitch, resolv.conf, systemd-resolved, mDNS) and cross-checks it against a direct DNS query, no LD_PRELOAD/eBPF/ptrace.  
[![Crates.io Version](https://badgen.net/crates/v/gai-inspector?color=e08b6c&icon=crates)](https://crates.io/crates/gai-inspector)
[![Release](https://badgen.net/github/release/casablanque-code/gai?color=1b6838)](https://github.com/casablanque-code/gai/releases/latest)
[![Crates.io Downloads](https://badgen.net/crates/d/gai-inspector?color=284b63)](https://crates.io/crates/gai-inspector)

* **[gai-core](https://crates.io/crates/gai-core)** — Pure parsing + simulation of Linux name-resolution config (nsswitch.conf, resolv.conf, gai.conf, hosts) behind gai-inspector — no I/O, fixture-tested.  
[![Crates.io Version](https://badgen.net/crates/v/gai-core?color=e08b6c&icon=crates)](https://crates.io/crates/gai-core)
[![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/gai-core/latest/gai_core/)
[![Crates.io Downloads](https://badgen.net/crates/d/gai-core?color=284b63)](https://crates.io/crates/gai-core)

* **[gai-probe](https://crates.io/crates/gai-probe)** — Real I/O backing gai-core's simulation: DNS queries, /etc/hosts, systemd-resolved D-Bus, one-shot mDNS probing.  
[![Crates.io Version](https://badgen.net/crates/v/gai-probe?color=e08b6c&icon=crates)](https://crates.io/crates/gai-probe)
[![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/gai-probe/latest/gai_probe/)
[![Crates.io Downloads](https://badgen.net/crates/d/gai-probe?color=284b63)](https://crates.io/crates/gai-probe)

* **[sidecheck](https://crates.io/crates/sidecheck)** — CLI that audits your own HTTP endpoints for remote timing side-channels, using proper statistics (bootstrap confidence intervals, robust jitter estimation) instead of a stopwatch.  
[![Crates.io Version](https://badgen.net/crates/v/sidecheck?color=e08b6c&icon=crates)](https://crates.io/crates/sidecheck)
[![Crates.io Downloads](https://badgen.net/crates/d/sidecheck?color=284b63)](https://crates.io/crates/sidecheck)

* **[sidecheck-core](https://crates.io/crates/sidecheck-core)** — Statistical core and HTTP sampler behind sidecheck: Crosby-Wallach box-test timing analysis as a standalone library.  
[![Crates.io Version](https://badgen.net/crates/v/sidecheck-core?color=e08b6c&icon=crates)](https://crates.io/crates/sidecheck-core)
[![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/sidecheck-core/latest/sidecheck_core/)
[![Crates.io Downloads](https://badgen.net/crates/d/sidecheck-core?color=284b63)](https://crates.io/crates/sidecheck-core)

* **[pcap-frame-parser](https://crates.io/crates/pcap-frame-parser)** — A small, dependency-light Rust parser for network capture files and the frames inside them - no `libpcap`/`npcap` linkage, no `unsafe`.  
[![Crates.io Version](https://badgen.net/crates/v/pcap-frame-parser?color=e08b6c&icon=crates)](https://crates.io/crates/pcap-frame-parser)
[![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/pcap-frame-parser/latest/pcap_frame_parser/)
[![Crates.io Downloads](https://badgen.net/crates/d/pcap-frame-parser?color=284b63)](https://crates.io/crates/pcap-frame-parser)

* **[Network Forensic Series](https://github.com/stars/casablanque-code/lists/network-forensics)** — A growing collection of browser-based postmortem PCAP analysis tools.

#### 🟢 Node.js
* **[@lighthouse-explorer/light-parser](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)** — Parses IALA maritime light characteristic strings into structured ASTs with computed phase sequences.  
[![npm Version](https://badgen.net/npm/v/@lighthouse-explorer/light-parser?color=901d38&icon=npm)](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)
[![npm Downloads](https://badgen.net/npm/dm/@lighthouse-explorer/light-parser?color=284b63)](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)

* **[burnafter](https://github.com/casablanque-code/burnafterread)** — CLI tool and Fullstack application to share secrets that safely burn after being read.  
[![npm Version](https://badgen.net/npm/v/burnafter?color=901d38&icon=npm)](https://www.npmjs.com/package/burnafter)
[![npm Downloads](https://badgen.net/npm/dm/burnafter?color=284b63)](https://www.npmjs.com/package/burnafter)

---
```text
================================================================================
PGP Fingerprint : 2A49 CD4A F95F 76DF 38FC 1F9E BFB3 5633 7514 9683
Status          : Open for Infrastructure Audits & Systems Engineering
================================================================================
