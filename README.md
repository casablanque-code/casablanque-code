### 📦 Open Source Packages

Lightweight utilities and production-ready tools:

#### 🔵 Go
* **[cfzt](https://github.com/casablanque-code/cfzt)** (`zt`) — Zero Trust tunnel manager. Automatically exposes local services through Cloudflare Zero Trust, manages system daemons, configures access policies, and auto-heals UDP/QUIC fallbacks.  
[![Go Reference](https://pkg.go.dev/badge/github.com/casablanque-code/cfzt.svg)](https://pkg.go.dev/github.com/casablanque-code/cfzt)
[![Gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/casablanque-code/cfzt/actions/workflows/gitleaks.yml)
[![Tiny Tool Town](https://img.shields.io/badge/featured-TinyToolTown-blue)](https://www.tinytooltown.com/tools/cfzt/)
[![Release](https://img.shields.io/github/v/release/casablanque-code/cfzt)](https://github.com/casablanque-code/cfzt/releases/latest)  

#### ⚪ C
* **[khm](https://github.com/casablanque-code/khm)** — Known Hosts Manager. A zero-dependency CLI tool to audit, diff, and scan SSH `known_hosts` using raw BSD sockets and a partial SSH handshake.  
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen)](#how-it-works)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey)](#install)
[![GitHub release](https://img.shields.io/github/v/release/casablanque-code/khm?color=blue&style=flat-square)](https://github.com/casablanque-code/khm/releases)
[![GitHub All Releases](https://img.shields.io/github/downloads/casablanque-code/khm/total?color=brightgreen&style=flat-square)](https://github.com/casablanque-code/khm/releases)

#### 🦀 Rust
* **[ios-config](https://crates.io/crates/ios-config)** — Parser and high-level wrapper for Cisco IOS configurations.  
[![Crates.io Version](https://img.shields.io/crates/v/ios-config?color=orange&style=flat-square)](https://crates.io/crates/ios-config)
[![docs.rs](https://img.shields.io/docsrs/ios-config?style=flat-square)](https://docs.rs/ios-config/latest/ios_config/)
[![Crates.io Downloads](https://img.shields.io/crates/d/ios-config?color=blue&style=flat-square)](https://crates.io/crates/ios-config)

* **[ios-config-core](https://crates.io/crates/ios-config-core)** — Intermediate representation (IR) types for parsed Cisco IOS configurations.  
[![Crates.io Version](https://img.shields.io/crates/v/ios-config-core?color=orange&style=flat-square)](https://crates.io/crates/ios-config-core)
[![docs.rs](https://img.shields.io/docsrs/ios-config-core?style=flat-square)](https://docs.rs/ios-config-core/0.1.0/ios_config_core/)
[![Crates.io Downloads](https://img.shields.io/crates/d/ios-config-core?color=blue&style=flat-square)](https://crates.io/crates/ios-config-core)

* **[gai-inspector](https://crates.io/crates/gai-inspector)** (`gai`) — getaddrinfo inspector: explains how a name turns into an IP (nsswitch, resolv.conf, systemd-resolved, mDNS) and cross-checks it against a direct DNS query, no LD_PRELOAD/eBPF/ptrace.  
[![Crates.io Version](https://img.shields.io/crates/v/gai-inspector?color=orange&style=flat-square)](https://crates.io/crates/gai-inspector)
[![Release](https://img.shields.io/github/v/release/casablanque-code/gai)](https://github.com/casablanque-code/gai/releases/latest)
[![Crates.io Downloads](https://img.shields.io/crates/d/gai-inspector?color=blue&style=flat-square)](https://crates.io/crates/gai-inspector)

* **[gai-core](https://crates.io/crates/gai-core)** — Pure parsing + simulation of Linux name-resolution config (nsswitch.conf, resolv.conf, gai.conf, hosts) behind gai-inspector — no I/O, fixture-tested.  
[![Crates.io Version](https://img.shields.io/crates/v/gai-core?color=orange&style=flat-square)](https://crates.io/crates/gai-core)
[![docs.rs](https://img.shields.io/docsrs/gai-core?style=flat-square)](https://docs.rs/gai-core/latest/gai_core/)
[![Crates.io Downloads](https://img.shields.io/crates/d/gai-core?color=blue&style=flat-square)](https://crates.io/crates/gai-core)

* **[gai-probe](https://crates.io/crates/gai-probe)** — Real I/O backing gai-core's simulation: DNS queries, /etc/hosts, systemd-resolved D-Bus, one-shot mDNS probing.  
[![Crates.io Version](https://img.shields.io/crates/v/gai-probe?color=orange&style=flat-square)](https://crates.io/crates/gai-probe)
[![docs.rs](https://img.shields.io/docsrs/gai-probe?style=flat-square)](https://docs.rs/gai-probe/latest/gai_probe/)
[![Crates.io Downloads](https://img.shields.io/crates/d/gai-probe?color=blue&style=flat-square)](https://crates.io/crates/gai-probe)

* **[sidecheck](https://crates.io/crates/sidecheck)** — CLI that audits your own HTTP endpoints for remote timing side-channels, using proper statistics (bootstrap confidence intervals, robust jitter estimation) instead of a stopwatch.  
[![Crates.io Version](https://img.shields.io/crates/v/sidecheck?color=orange&style=flat-square)](https://crates.io/crates/sidecheck)
[![Crates.io Downloads](https://img.shields.io/crates/d/sidecheck?color=blue&style=flat-square)](https://crates.io/crates/sidecheck)

* **[sidecheck-core](https://crates.io/crates/sidecheck-core)** — Statistical core and HTTP sampler behind sidecheck: Crosby-Wallach box-test timing analysis as a standalone library.  
[![Crates.io Version](https://img.shields.io/crates/v/sidecheck-core?color=orange&style=flat-square)](https://crates.io/crates/sidecheck-core)
[![docs.rs](https://img.shields.io/docsrs/sidecheck-core?style=flat-square)](https://docs.rs/sidecheck-core/latest/sidecheck_core/)
[![Crates.io Downloads](https://img.shields.io/crates/d/sidecheck-core?color=blue&style=flat-square)](https://crates.io/crates/sidecheck-core)  

* **[pcap-frame-parser](https://crates.io/crates/pcap-frame-parser)** — A small, dependency-light Rust parser for network capture files and the frames inside them - no `libpcap`/`npcap` linkage, no `unsafe`.  
[![Crates.io Version](https://img.shields.io/crates/v/pcap-frame-parser?color=orange&style=flat-square)](https://crates.io/crates/pcap-frame-parser)
[![docs.rs](https://img.shields.io/docsrs/pcap-frame-parser?style=flat-square)](https://docs.rs/pcap-frame-parser/0.2.1/pcap_frame_parser/)
[![Crates.io Downloads](https://img.shields.io/crates/d/pcap-frame-parser?color=blue&style=flat-square)](https://crates.io/crates/pcap-frame-parser)

* **[Network Forensic Series](https://github.com/stars/casablanque-code/lists/network-forensics)** — A growing collection of browser-based postmortem PCAP analysis tools.

#### 🟢 Node.js
* **[@lighthouse-explorer/light-parser](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)** — Parses IALA maritime light characteristic strings into structured ASTs with computed phase sequences.  
[![npm Version](https://img.shields.io/npm/v/@lighthouse-explorer/light-parser?color=green&style=flat-square)](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)
[![npm Downloads](https://img.shields.io/npm/dm/@lighthouse-explorer/light-parser?color=blue&style=flat-square)](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)

* **[burnafter](https://github.com/casablanque-code/burnafterread)** — CLI tool and Fullstack application to share secrets that safely burn after being read.  
[![npm Version](https://img.shields.io/npm/v/burnafter?color=green&style=flat-square)](https://www.npmjs.com/package/burnafter)
[![npm Downloads](https://img.shields.io/npm/dm/burnafter?color=blue&style=flat-square)](https://www.npmjs.com/package/burnafter)
