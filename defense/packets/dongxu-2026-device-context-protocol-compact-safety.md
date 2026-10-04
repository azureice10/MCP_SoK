# Evidence Locator Packet: dongxu-2026-device-context-protocol-compact-safety

- **Title**: Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.26159
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\dongxu-2026-device-context-protocol-compact-safety\fulltext.txt
- **Character Count**: 49173

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 5895:5943]
> This paper makes the following contributions:
> 1.
**Location**: `Abstract` [offsets: 8202:8403]
> com/device-context-protocol/dcp; the Python Bridge ships on PyPI as pydcp; the corpus,
> validators, and bench harnesses behind every figure in this paper are in the same repo and
> re-runnable end-to-end.

## Block 3: Method Locator
**Section Heading**: `A Compact, Safety-First Architecture for` [section offsets: 1899:2008]
**First 120 words verbatim** [offsets: 1899:2762]
> A Compact, Safety-First Architecture for
> LLM-Driven Control of Constrained Devices
> 
> Dongxu Yang∗1
> 
> May 2026
> 
> Abstract
> 
> 1
> 
> The deployment of large language models (LLMs) as orchestrators of external tools has driven
> the rapid adoption of standardized invocation protocols. The Model Context Protocol (MCP) [1]
> has emerged as a leading candidate, providing a JSON-RPC–based interface for exposing tools,
> resources, and prompts to LLM clients such as Claude Desktop, IDE assistants, and agent
> frameworks. The MCP roadmap for 2026 [14] foregrounds enterprise readiness: stateless HTTP
> transport, OAuth 2.1, audit logging, and gateway architectures. It says nothing about embedded
> devices, and there is no indication that the upstream specification will descend to that layer.
> 
> This produces a gap. Physical devices—smart-home actuators, sensors, laboratory equipment,
**Section Heading**: `Architecture` [section offsets: 12063:12165]
**First 120 words verbatim** [offsets: 12063:12825]
> Architecture
> 
> Bridge  
>   sole trust boundary
> 
> MCP
> 
> Capability token
> Range / type check
> 
> LLM
> MCP host
> 
> results
> 
> Dry-run preview
> Audit / rate-limit
> 
> 3.2
> Wire format
> 
> DCP wire
> 
> Device
> commodity MCU
> 
> reply
> 
> UART · MQTT · BLE · USB-CDC
> 
> one wire format, any transport
> 
> 4
> 
> Figure 1: DCP architecture. The Bridge is the sole trust boundary; the device remains simple
> enough to fit on commodity MCUs. The same wire format works across multiple transports.
> 
> The Bridge is not optional. Devices are not expected to verify capability tokens themselves
> in v0.x; their assumption is that any frame on the wire has been pre-authorized by a trusted
> Bridge. (Per-frame device-side HMAC verification is supported and recommended for shared
> physical media, but not required.) This
**Section Heading**: `Implementation` [section offsets: 21822:32165]
**First 120 words verbatim** [offsets: 21822:22517]
> Implementation
> 
> 4.1
> Python Bridge
> 
> 7
> 
> A note on why OpenAPI appears in the comparison at all. OpenAPI is included as an
> upper-bound reference for what a mature server-side validation layer can structurally express —
> 
> not as a deployable alternative for the targets DCP serves. A typical OpenAPI runtime needs
> an HTTP server, a JSON parser, URL routing, and (for pattern) a regex engine, comfortably
> three orders of magnitude beyond what fits on the MCUs in scope here (DCP’s device-side
> runtime measures 27.6 KB flash and 0.6 KB RAM on an ESP32, Figure 5 below; comparable
> HTTP/OpenAPI stacks need tens of MB of RAM alone). So “DCP ties OpenAPI” is not a wash
> — it is the point: DCP delivers the

## Block 4: Evaluation Locator
**Section Heading**: `results` [section offsets: 12165:13911]
**First 120 words verbatim** [offsets: 12165:12926]
> results
> 
> Dry-run preview
> Audit / rate-limit
> 
> 3.2
> Wire format
> 
> DCP wire
> 
> Device
> commodity MCU
> 
> reply
> 
> UART · MQTT · BLE · USB-CDC
> 
> one wire format, any transport
> 
> 4
> 
> Figure 1: DCP architecture. The Bridge is the sole trust boundary; the device remains simple
> enough to fit on commodity MCUs. The same wire format works across multiple transports.
> 
> The Bridge is not optional. Devices are not expected to verify capability tokens themselves
> in v0.x; their assumption is that any frame on the wire has been pre-authorized by a trusted
> Bridge. (Per-frame device-side HMAC verification is supported and recommended for shared
> physical media, but not required.) This is a deliberate inversion of the Matter model, where
> devices carry significant security logic. DCP’s

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `results` [offsets: 13157:13231]
> The bottom of
> Figure 2 compares typical on-wire size with three baselines.
**Location**: `results` [offsets: 13625:13709]
> Figure 2: DCP frame layout and on-wire size compared to representative alternatives.

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
**Section Heading**: `Discussion and Limitations` [section offsets: 39518:43100]
**First 120 words verbatim** [offsets: 39518:40318]
> Discussion and Limitations
> 
> 6.1
> What this paper does not prove
> 
> 12
> 
> We have validated the reference implementation on one MCU (ESP32-WROOM-32) over one
> 
> transport (UART), reported its compiled footprint, measured its end-to-end latency, and run an
> empirical adversarial-prompt study against five LLMs across four vendors using AgentDojo’s
> attack templates (Section 3.4, Figure 3). We have not established:
> • Footprint and latency across the multi-MCU matrix that IoT-MCP covers (Cortex-M0+,
> nRF52840, ESP32-C3 etc.). The DCP firmware is portable Arduino C++, but only ESP32 is
> measured here.
> • Full-stack end-to-end latency including the LLM API call (which is what IoT-MCP’s
> ∼205 ms [22] number measures). Our wire-level A/B in Section 4 shows DCP and IoT-
> MCP’s UART-JSON tie on the host↔device leg

## Block 9: Adaptivity Hits
no hits
