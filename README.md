# Engineering, mostly at the edges of intuition

<!-- AUTO-GENERATED-STATUS -->
🔴 **Radar status:** 4 findings today
<!-- /AUTO-GENERATED-STATUS -->

---

I build small tools around systems where the obvious explanation is often not quite true.

DNS, SSH, Zero Trust, timing, packet captures, configuration formats, infrastructure - things we've had for years and think we already understand.

Usually it starts with:

> **"Is that actually what happens?"**

Then I go find out. **friction → investigation → hypothesis → tool.** The tool is just the artifact.

---

## Live Radar (based on [gai](https://github.com/casablanque-code/gai))

<!-- AUTO-GENERATED -->

**Resolution divergence** (`gai doctor` per-domain reality check) - last run `2026-08-30 10:54 UTC`
> 18 divergence(s) in the last 4 days across 14 tracked domains -- most recent on 2026-08-30.
> _(mostly anycast/GeoDNS edges disagreeing between two queries -- [full per-domain log for 2026-08-30](https://github.com/casablanque-code/casablanque-code/blob/main/.radar/raw-20260830.log))_

<!-- /AUTO-GENERATED -->

<!-- AUTO-GENERATED-SIG -->

**README integrity** · signed `2026-08-30 11:41 UTC` · [verify](https://github.com/casablanque-code/casablanque-code/blob/main/README.stable.md.sig)
> `SHA256: 51398c4a1116350f…` · [my PGP key](https://keys.openpgp.org/search?q=2A49CD4AF95F76DF38FC1F9EBFB3563375149683)
> Zero Trust isn't just for infra. Don't trust this file either -- verify it.

<!-- /AUTO-GENERATED-SIG -->


<!-- AUTO-GENERATED-LEADERBOARD -->

**Most disagreeing domains (30 days)**

| Domain | Divergences |
| :--- | ---: |
| `google.com` | 4 |
| `netflix.com` | 4 |
| `ipv6.google.com` | 4 |
| `github.com` | 3 |
| `akamai.com` | 3 |

<!-- /AUTO-GENERATED-LEADERBOARD -->

---

### Trust & Identity

We usually treat trust as a fact.
Turns out, it's something systems have to fucking keep proving.

* **[khm](https://github.com/casablanque-code/khm)** - `known_hosts` is not just a cache. It's a database of server identities.
* **[cfzt](https://github.com/casablanque-code/cfzt)** - Zero Trust is less about replacing a VPN and more about identity, reachability and continuously verifying state.
* **[gai](https://github.com/casablanque-code/gai)** - `dig` working doesn't mean your process resolves the name the same way. Reconstructs the actual `getaddrinfo()` decision path.
* **[burnafterread](https://github.com/casablanque-code/burnafterread)** - sharing a secret doesn't have to mean giving the server access to it. [`live`](https://burnafterread.casablanque.com/)
### Measurement

We usually treat latency as noise.
Turns out, sometimes the measurement is the attack surface.  

* **[sidecheck](https://github.com/casablanque-code/sidecheck)** - remote timing side-channel detection using statistics instead of a stopwatch.

### Network Forensics

Packets are evidence, not truth.

**[Network Forensics Series](https://github.com/stars/casablanque-code/lists/network-forensics)**

* **[ospf-postmortem](https://github.com/casablanque-code/ospf-postmortem)** - reconstruct the OSPF FSM and find why an adjacency got stuck. [`live`](https://ospf.postmortem.casablanque.com/)
* **[dhcp-postmortem](https://github.com/casablanque-code/dhcp-postmortem)** - reconstruct DORA and detect failures from packet evidence. [`live`](https://dhcp.postmortem.casablanque.com/)
* **[stp-postmortem](https://github.com/casablanque-code/stp-postmortem)** - reconstruct STP/RSTP behaviour, topology changes and root causes. [`live`](https://stp.postmortem.casablanque.com/)
* **[dns-postmortem](https://github.com/casablanque-code/dns-postmortem)** - DNS traffic, anomaly detection and tunneling analysis. [`live`](https://dns.postmortem.casablanque.com/)
> *Everything runs locally in the browser. PCAPs never leave the machine.*

### Semantics & Infrastructure

Some problems look like parsing or automation problems until you look closer.
But most "automation" is just someone's assumptions, hardcoded and left to rot.

* **[netconv](https://github.com/casablanque-code/netconv)** - configuration conversion is about semantics, not replacing keywords.
* **[pcap-frame-parser](https://github.com/casablanque-code/pcap-frame-parser)** - packet formats have decades of edge cases hiding behind deceptively simple structures.
* **[platform-infra](https://github.com/casablanque-code/platform-infra)** - self-service infrastructure for small teams, without turning the sysadmin into an API.

---

<details>
<summary>A few libs</summary>

| Library / Package | Version | Docs | Downloads |
| :--- | :--- | :--- | :--- |
| **[gai-core](https://crates.io/crates/gai-core)** | [![Crates.io Version](https://badgen.net/crates/v/gai-core?color=e08b6c&icon=crates)](https://crates.io/crates/gai-core) | [![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/gai-core/latest/gai_core/) | [![Crates.io Downloads](https://badgen.net/crates/d/gai-core?color=284b63)](https://crates.io/crates/gai-core) |
| **[gai-probe](https://crates.io/crates/gai-probe)** | [![Crates.io Version](https://badgen.net/crates/v/gai-probe?color=e08b6c&icon=crates)](https://crates.io/crates/gai-probe) | [![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/gai-probe/latest/gai_probe/) | [![Crates.io Downloads](https://badgen.net/crates/d/gai-probe?color=284b63)](https://crates.io/crates/gai-probe) |
| **[sidecheck-core](https://crates.io/crates/sidecheck-core)** | [![Crates.io Version](https://badgen.net/crates/v/sidecheck-core?color=e08b6c&icon=crates)](https://crates.io/crates/sidecheck-core) | [![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/sidecheck-core/latest/sidecheck_core/) | [![Crates.io Downloads](https://badgen.net/crates/d/sidecheck-core?color=284b63)](https://crates.io/crates/sidecheck-core) |
| **[netconv-core](https://crates.io/crates/netconv-core)** | [![Crates.io Version](https://badgen.net/crates/v/netconv-core?color=e08b6c&icon=crates)](https://crates.io/crates/netconv-core) | [![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/netconv-core/latest/netconv_core/) | [![Crates.io Downloads](https://badgen.net/crates/d/netconv-core?color=284b63)](https://crates.io/crates/netconv-core) |
| **[pcap-frame-parser](https://crates.io/crates/pcap-frame-parser)** | [![Crates.io Version](https://badgen.net/crates/v/pcap-frame-parser?color=e08b6c&icon=crates)](https://crates.io/crates/pcap-frame-parser) | [![docs.rs](https://badgen.net/badge/docs/rs/343a40)](https://docs.rs/pcap-frame-parser/latest/pcap_frame_parser/) | [![Crates.io Downloads](https://badgen.net/crates/d/pcap-frame-parser?color=284b63)](https://crates.io/crates/pcap-frame-parser) |
| **[burnafter](https://github.com/casablanque-code/burnafterread)** | [![npm Version](https://badgen.net/npm/v/burnafter?color=901d38&icon=npm)](https://www.npmjs.com/package/burnafter) | — | [![npm Downloads](https://badgen.net/npm/dt/burnafter?color=284b63)](https://www.npmjs.com/package/burnafter) |
| **[@lighthouse-explorer/light-parser](https://www.npmjs.com/package/@lighthouse-explorer/light-parser)** | [![npm Version](https://badgen.net/npm/v/@lighthouse-explorer/light-parser?color=901d38&icon=npm)](https://www.npmjs.com/package/@lighthouse-explorer/light-parser) | — | [![npm Downloads](https://badgen.net/npm/dt/@lighthouse-explorer/light-parser?color=284b63)](https://www.npmjs.com/package/@lighthouse-explorer/light-parser) |

</details>

---

[PGP](https://keys.openpgp.org/search?q=2A49CD4AF95F76DF38FC1F9EBFB3563375149683) · [Stack](https://stackshare.io/casablanque-code/engineer-stack)

---

[![Ko-fi](https://badgen.net/badge/support/ko-fi/e74c3c?icon=kofi&labelColor=2d3748)](https://ko-fi.com/casablanque)
