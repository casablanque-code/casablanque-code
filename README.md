# Andrew · casablanque-code

Network/security engineer. I build tools that check whether the obvious
explanation is actually true, and a few systems that just have to work.

[casablanque.com](https://casablanque.com) · [casablanque@proton.me](mailto:casablanque@proton.me) · [PGP](https://keys.openpgp.org/search?q=2A49CD4AF95F76DF38FC1F9EBFB3563375149683) · [Ko-fi](https://ko-fi.com/casablanque)

## Featured

### [A.V.E.N.G.E](https://github.com/casablanque-code/avenge): edge vibration analytics

Go engine that runs next to the sensor: FFT → SDT compression → Z-score
anomaly detection. Zero dependencies, zero-allocation hot path.
MQTT → ClickHouse → Grafana, one `docker compose up` for the core stack.

## Products

- [**railcast**](https://github.com/casablanque-code/railcast): hosted appcast and update delivery for Sparkle apps. One command to publish, signed feed, Cloudflare Workers + R2. [`live`](https://railcast.casablanque.com)
- [**komposer**](https://github.com/casablanque-code/komposer): terminal UI for Docker Compose files with spec validation and security checks.
- [**platform-infra**](https://github.com/casablanque-code/platform-infra): self-service infrastructure for small teams on Cloudflare Workers + D1 + R2.

## Investigations

> friction → investigation → hypothesis → tool

- [**gai**](https://github.com/casablanque-code/gai): `dig` working doesn't mean your process resolves the name the same way. Reconstructs the real `getaddrinfo()` decision path.
- [**khm**](https://github.com/casablanque-code/khm): `known_hosts` is a database of server identities, not a cache.
- [**cfzt**](https://github.com/casablanque-code/cfzt): Cloudflare Zero Trust from the command line.
- [**sidecheck**](https://github.com/casablanque-code/sidecheck): remote timing side-channel detection using statistics instead of a stopwatch.
- [**burnafterread**](https://github.com/casablanque-code/burnafterread): share a secret without giving the server access to it. [`live`](https://burnafterread.casablanque.com/)
- [**netconv**](https://github.com/casablanque-code/netconv): config conversion is about semantics, not replacing keywords.

### Network forensics

Packets are evidence, not truth. Everything runs in the browser; PCAPs never leave your machine.

[ospf](https://ospf.postmortem.casablanque.com/) · [dhcp](https://dhcp.postmortem.casablanque.com/) · [stp](https://stp.postmortem.casablanque.com/) · [dns](https://dns.postmortem.casablanque.com/)

---

Zero Trust isn't just for infra. Don't trust this file either, verify it.

<details>
<summary>Verify this README</summary>

```
gpg --keyserver keys.openpgp.org --recv-keys 2A49CD4AF95F76DF38FC1F9EBFB3563375149683
curl -sO https://raw.githubusercontent.com/casablanque-code/casablanque-code/main/README.md
curl -sO https://raw.githubusercontent.com/casablanque-code/casablanque-code/main/README.md.sig
gpg --verify README.md.sig README.md
```

</details>
