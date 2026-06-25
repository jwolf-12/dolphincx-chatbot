# DolphinCX (SignalDesk) Platform — Combined Knowledge Base

**Source:** Merged and deduplicated from three source documents (platform features overview, call center operations overview, and unified user/admin/API guide).
**Purpose:** Single consolidated reference for RAG retrieval.

---

## 1. Product Overview

DolphinCX (also known as SignalDesk), developed by Nouveau Labs Inc., is a cloud-based contact center and video conferencing platform that unifies voice calling, video calling, and chat-based communication across customer-facing and internal channels. It supports inbound customer support, outbound calling campaigns, and movement between channels, allowing a single conversation to flow between chat, voice, and video without losing context.

The platform handles both inbound customer support and outbound agent-initiated calls, and supports customer-to-agent calls, agent-to-agent calls, and video calls. An ongoing audio call can be escalated to audio-video mid-conversation without dropping or restarting the call.

Every call — inbound, outbound, agent-to-agent, or video — is automatically recorded and transcribed as soon as the agent accepts it. No manual step is required to start or stop recording or transcription.

Beyond traditional call handling, the platform layers AI capabilities across the conversation lifecycle:

- **Virtual agents** (flow-based, NLP-based, and GenAI-based) can handle conversations independently or alongside human agents.
- **Agent Assist** provides real-time guidance to agents during live interactions.
- **Post-conversation AI features** such as call summaries, sentiment classification, emotion detection, and AI-powered search make it possible to analyze and retrieve information across large volumes of recorded calls and chats.

The platform also integrates with external ticketing and CRM systems, supports messaging channels such as WhatsApp, and gives administrators tools for provisioning virtual numbers, masking phone numbers, and self-onboarding new accounts. Real-time dashboards and historical analytics give supervisors visibility into agent activity, call volumes, and customer sentiment across both human-agent and virtual-agent interactions.

A typical inbound call flow: customer dials in → IVR/ICR sequence plays → ACD routes the call to an available agent → agent receives a real-time notification → upon acceptance, recording and transcription begin automatically.

### Full Feature List

- Inbound Calling with ACD
- Outbound Calling and Campaigns
- Video Support / Video Calling
- Call Transfer
- Barging, Monitoring, and Whispering
- IVR and ICR
- Voice Mail
- Click to Dial
- N-way Calling
- Built-in Conferencing
- Recording, Transcription, and AI-Powered Search
- Real-time Call Monitoring (Live Dashboard)
- Extensive Reports / Analytics
- Failover from Data Calls to PSTN Calls
- Chat Support with ACD (1-1 and Group Chat)
- Movement across Chats and Calls
- Movement across Virtual and Human Agents
- Flow-based, NLP-based, and GenAI-based Virtual Agents
- Agent Assist
- Emotion Detection
- Call Summary (AI Dialogue Summary)
- Ticketing System and CRM Integration
- Number Masking and Virtual Numbers
- WhatsApp Integration
- Self-Signup

---

## 2. Inbound Calling, ACD, and IVR/ICR

Inbound calling handles all customer-initiated voice calls into the contact center. Incoming calls are managed by **Automatic Call Distribution (ACD)**, which assigns each call to an available agent based on configured routing rules such as skill, availability, or queue priority.

Before a call reaches an agent, it passes through an **Interactive Voice Response (IVR)** and **Interactive Call Routing (ICR)** sequence. IVR plays an automated menu and collects customer input via keypad selections; ICR uses that input to determine which queue, department, or agent the call should be routed to. This sequence runs automatically as a standard part of every inbound call.

Once IVR/ICR completes and ACD assigns the call, the receiving agent gets a real-time call notification. When the agent accepts, recording and transcription begin automatically — no manual action required.

Agent-to-agent inbound calls are supported through the same routing infrastructure, enabling internal transfers and direct communication between agents in addition to customer-facing calls.

---

## 3. Outbound Calling and Campaigns

Outbound calling allows agents to initiate calls to customers, commonly used for callbacks (when agents were unavailable during the original inbound call), follow-ups, and proactive outreach.

A **campaign** is a configured outbound initiative with an assigned list of customer phone numbers for agents to dial. Campaigns are created with a name and description, and customer numbers are loaded into the campaign for dialing. Multiple campaigns can exist within the system, but typically only one runs as the active/open campaign at a time.

Campaign data can be filtered for reporting using duration ranges: **Today, Last One Week, Last One Month, Last One Year, Select Month, Select Year, Select Date, and Until Now.**

### Outbound Live Dashboard

A dedicated Outbound/Campaign view on the live dashboard provides real-time visibility into campaign performance, displaying:

- Calls in Queue
- Active Calls
- Abandoned/Dropped Calls
- Agents Available
- Call Rate (line chart over time)
- Call Results
- Realtime Call Monitoring count
- Calls Silence
- Successful Calls
- Failed Calls
- Ongoing Calls

---

## 4. Click to Dial and N-way Calling

**Click to Dial** lets agents place outbound calls directly from the platform interface, without dialing manually on a separate device. Two dialing methods:

- **Direct dial:** Enter the customer's phone number into the dialpad and place the call.
- **Contact search:** Search for another agent or customer by name or email, select from the results list, and initiate the call.

The contact list surfaced in the dialpad includes: Customer ID, Name, Customer Type (e.g., Individual), Email ID, Mobile Number, and Address.

**N-way calling** extends an active call to additional participants. There is no fixed limit on the number of participants (N); agents can add internal colleagues or external customers to a live call as needed from the dialpad, which presents a searchable contacts list for quick selection.

---

## 5. Built-in Conferencing

In addition to ad-hoc N-way calling, the platform provides built-in conferencing for structured multi-party sessions — bringing together multiple internal and external participants (e.g., a specialist, manager, or several stakeholders) without relying on a separate third-party conferencing tool.

Because conferencing runs on the same platform that handles calls, chats, and video, conference sessions are recorded and transcribed using the same infrastructure as standard calls, and participants can be added using the same contact search used for click to dial and N-way calling.

---

## 6. Call Transfer, Hold/MOH, and Voice Mail

**Call transfer** allows an agent to hand off an active call to another agent or department, connecting the receiving party directly to the ongoing conversation — a seamless handoff without requiring the customer to disconnect and call back.

**Call hold / Music on Hold (MOH):** Agents can place a customer on hold at any point during a call. While on hold, an MOH message plays. The default message is:

> "We appreciate your patience. Your call means a lot to us. Please hold and we will be with you as soon as possible."

This message is fully customizable by administrators (see also Custom MOH Settings, Section 16).

**Voice mail** allows customers to leave a recorded message when no agent is available. Messages are stored within the platform and remain accessible to agents and administrators for follow-up, ensuring calls that can't be answered live are still captured and actioned.

---

## 7. Video Support

The platform supports video calling in addition to audio. Customer-to-agent and agent-to-agent conversations can take place over video, and an ongoing audio call can be escalated to audio-video mid-conversation without dropping or restarting the call.

Video calls follow the same underlying call handling as audio calls: they can be transferred, recorded, and transcribed, and they appear in the same live dashboard and reporting views as voice interactions, allowing supervisors to monitor video-based conversations alongside audio and chat traffic without needing a separate tool.

---

## 8. Recording, Transcription, and AI-Powered Search

Every call — inbound, outbound, agent-to-agent, or video — is automatically recorded and transcribed as soon as the agent accepts it. No manual step is needed to start or stop either process.

Building on this archive of recordings and transcripts, **AI-powered search** allows users to search across recorded calls and group chat conversations using natural language queries rather than browsing recordings manually. This makes it possible to locate specific conversations — for example, calls where a particular topic, complaint, or phrase came up — across large volumes of historical recordings and chat threads, supporting both quality review and knowledge retrieval use cases.

---

## 9. Barging, Monitoring, and Whispering (Supervisor Controls)

Supervisors and administrators can observe or intervene in live calls from the Live Dashboard using three modes:

- **Monitoring:** The supervisor silently listens to a live call without either party being aware.
- **Whispering:** The supervisor speaks directly to the agent without the customer hearing.
- **Barging:** The supervisor joins the call as an active participant, audible to both agent and customer.

While monitoring a call, the supervisor can also view the live transcription of the conversation in real time.

---

## 10. Live Dashboard (Real-time Call Monitoring)

### 10.1 Overview

The Live Dashboard gives supervisors real-time visibility into all call center activity, organized into tabs/views: **Admin, Agent, Inbound Call, Outbound/Campaign, and Sequence List.**

### 10.2 Key Metrics

- Total Agents
- Agents Online
- Agents on Call
- Agents Offline
- Calls Waiting
- Calls in Queue

### 10.3 Agent Activity Stats

An Agent Activity Stats donut chart displays a breakdown of current agent statuses, giving supervisors an at-a-glance view of workforce availability.

### 10.4 Call Trends

The Call Trends chart tracks call volumes on a per-hour basis throughout the day, covering Inbound Calls, Outbound Calls, Dropped Calls, and Engaged Calls. Hovering over a data point shows a tooltip with specific counts (e.g., 14:00 — Inbound Calls: 2, Outbound Calls: 0, Dropped Calls: 0).

### 10.5 Supervisor Controls

From the Live Dashboard, supervisors can barge into or monitor any ongoing call, with live transcription visible directly within the dashboard view.

### 10.6 Live Chat Dashboard

A separate Live Chat Dashboard mirrors the Live (call) Dashboard concept but is focused on the chat channel — showing active chats, waiting customers, and agent chat loads.

---

## 11. Agent Status and Color Coding

Each agent's availability is tracked through a status system with visual color indicators:

| Status | Indicator / Effect |
|---|---|
| Available | Green — ready to receive incoming interactions across assigned call/chat flows |
| Do Not Disturb | Red — enforces immediate routing blocks on all incoming interactions |
| Be Right Back | Yellow/orange — short temporary absence signal |
| In a Call | Separate status indicator |
| Offline | Grey — deactivates agent footprint; disconnected from routing logic |
| Lunch Break | Extended absence; see Lunch Break Logic below |
| Tea Break / Bio Break | Short breaks; interactions are not routed |
| Training Break | Agent is in training; interactions are not routed |
| Custom statuses | Organization-defined (e.g., Fun, Jiffiy, Fetching) |

**Lunch Break Logic:** When an agent sets their status to Lunch, a 30-minute allowance begins. After 30 minutes without returning, the status indicator turns yellow as a warning. If the agent has not returned after an additional 10 minutes (40 minutes total), the status turns red to alert supervisors.

---

## 12. Customer Profile, Notes, and AI Dialogue Summary

### 12.1 Customer Profile

Each call is associated with a customer profile containing: Customer Name, Customer Type (e.g., Individual), Portal ID, Email Address, and Phone Number. The profile view includes two primary tabs: **Customer Info** and **List of Tickets**.

### 12.2 Notes and Comments

Agents can add notes to a customer record during or after a call via a notes panel with a template selector (a Default Template is available out of the box) and a comment input field. Agents can also add free-form comments via an "Add Comments" section.

### 12.3 AI Dialogue Summary / Call Summary

After a call or chat concludes, the platform automatically generates an AI-based summary capturing the key points of the interaction, without requiring manual note-taking throughout. Agents can review and edit the auto-generated summary before it's finalized. Once confirmed, the summary — along with its associated event type and template — is pushed automatically to the integrated CRM system, keeping customer records up to date without duplicate manual entry.

---

## 13. HD Tickets and CRM Integration

The platform integrates with external ticketing and CRM systems so that information captured during conversations (call summaries, notes, comments) is automatically pushed to the connected CRM, keeping customer records synchronized without manual re-entry.

The **HD Tickets** section, accessible under the List of Tickets tab within a customer profile, provides a paginated table of all support tickets associated with the customer or organization, with columns: **Ticket ID, Subject, Raised By, Status, Priority, Assigned To, and Date Raised On.** The system supports large ticket volumes, with pagination across potentially hundreds of pages.

A connected CRM status indicator on the Agent Home screen shows whether the CRM integration is currently active; when connected, customer data surfaces automatically when a call or chat arrives, giving agents context without manual lookups.

---

## 14. Extensive Reports and Analytics (Historical)

### 14.1 Overview

The reporting suite (Call Centre Reports) provides historical analytics across all call, chat, and video activity, organized into views: **Records List, Admins/Campaign, Live Score, All Score, All Agents, Inbound, and Outbound.**

### 14.2 Summary Statistics

- Total Calls
- Calls Answered
- Calls Missed
- Calls Rejected
- Calls Unanswered
- Average Call Duration
- Average Call Ring Duration
- Average Call Wait Duration

### 14.3 Sentiment Analysis and Emotion Detection

Each call record includes a sentiment classification. Tracked categories: **Delighted, Happy, Neutral, Disengaged, Angry, Abusive, and Bad.** Sentiment counts are displayed as part of summary rows/views.

**Emotion detection** analyzes the tone and content of a conversation in real time to gauge the customer's emotional state during a call or chat. These real-time signals feed into the same sentiment categories used in reporting and can prompt supervisor attention — for example, flagging a call where sentiment is trending negative so intervention (monitoring, whispering, barging) can happen before an issue escalates.

### 14.4 Call Trace Records

A Call Trace Records table provides a detailed log of individual calls: **Caller ID, Direction (e.g., Inbound), Agent, Flow, Start Time, Duration, and Status (Active, Ended, or Received).** A dedicated Abandoned Calls Reports view is also available.

---

## 15. Failover from Data Calls to PSTN Calls

To maintain call continuity over unreliable internet connections, the platform automatically fails over from internet-based (data) calls to PSTN (Public Switched Telephone Network) calls if a connectivity issue is detected. This failover happens automatically, without requiring the agent or customer to redial, helping ensure calls are not dropped due to network issues on either side.

---

## 16. Chat, WhatsApp, and Channel Movement

### 16.1 Chat Support with ACD

Text-based chat is supported alongside voice and video, routed through the same ACD system used for calls (**Chat ACD**), ensuring consistent queue management and agent assignment across channels. Both one-to-one and group chat sessions are supported.

### 16.2 Movement Across Chats and Calls

Agents can transition a conversation between chat and voice without the customer needing to re-initiate contact or repeat information, preserving context as the interaction moves between channels.

### 16.3 Movement Across Virtual and Human Agents

This concept extends to AI virtual agents: a conversation that begins with a flow-based, NLP-based, or GenAI-based virtual agent can be handed off to a human agent, and vice versa, while retaining conversation history and context — so customers don't need to restart the interaction when escalated to or returned from a human agent.

### 16.4 WhatsApp Integration

The platform integrates with WhatsApp, letting customers start and continue conversations over WhatsApp alongside other chat channels. WhatsApp conversations are routed through the same chat ACD as other chat traffic, reaching available agents via the same queue and routing rules. Because WhatsApp is handled within the same unified interface, WhatsApp conversations can also take advantage of movement across chats/calls, virtual agent handling, and AI features like summaries and sentiment tracking.

---

## 17. Virtual Agents and Agent Assist

### 17.1 Virtual Agent Types

The platform supports three categories of AI virtual agents, handling interactions on voice, chat, or both:

- **Flow-based virtual agents:** Follow predefined conversation paths built using a visual flow/decision-tree structure. Best suited to structured processes (collecting information, confirming details, guiding through a fixed sequence) where conversation paths are known in advance.
- **NLP-based virtual agents:** Use natural language processing to interpret free-form customer input rather than relying solely on fixed menu options. They identify customer intent and extract relevant entities (order numbers, dates, account details) from natural language, enabling more flexible conversations.
- **GenAI-based virtual agents:** Use generative AI to handle open-ended conversations, generating dynamic responses rather than selecting from fixed pre-written replies. They can draw on the platform's knowledge base to ground responses in accurate, up-to-date information.

All three types integrate with the platform's ACD, movement, and handoff mechanisms, so a virtual-agent-handled conversation can be escalated to a human agent when needed.

### 17.2 Agent Assist

Agent Assist provides real-time AI support to human agents during live calls and chats. As a conversation progresses, it can surface relevant knowledge base articles, suggested responses, and next-step recommendations based on what the customer is saying — helping agents respond accurately without manually searching for information mid-conversation.

By drawing on the same knowledge base and conversation history used by virtual agents, Agent Assist helps maintain consistency between bot and human-agent answers, and can reduce average handle time by reducing the need to place customers on hold while looking up information.

### 17.3 Virtual Agent Management (Admin)

Configured under **Tenant Admin > Contact Center Management:**

- **Flow Scripts:** Reusable script definitions used to build virtual agent flows (added with name, ID, descriptive metadata).
- **Flow Resources** (selected via a "Choose Flow" selector):
  - **Intents** — define what the virtual agent can recognize and respond to (e.g., "check order status," "speak to agent").
  - **FAQs** — pre-defined question-answer pairs served directly without triggering complex script trees.
  - **Corpus & NLP Corpus** — training dataset text blocks used to improve natural language understanding.
  - **Regexes & NLP Regexes** — patterns for text evaluation, entity extraction, or input validation (e.g., matching order IDs).
  - **NLP Taggings** — rules to label and classify entities/text segments within NLP processing.
- **Virtual Agents Table:** Automated bots configured for inbound/outbound systems, supporting manual Add forms (User ID, First Name) and bulk file imports.

---

## 18. Number Masking and Virtual Numbers

**Virtual numbers** are phone numbers provisioned through the platform (rather than tied to a physical SIM/line) that can be assigned to campaigns, departments, or regions for inbound and outbound calling — allowing organizations to operate local or toll-free numbers across geographies without managing physical telecom infrastructure for each one.

**Number masking** builds on virtual numbers to protect privacy: instead of exposing a customer's or agent's real phone number during a call, the platform routes the call through a virtual number so neither party sees the other's actual number. Useful for scenarios where two parties need to communicate by phone (e.g., a delivery agent and customer) without either side gaining permanent access to the other's real contact details.

### Caller ID Masking Rules (Admin)

| Direction | Masking Options |
|---|---|
| Incoming Calls | Controlled via Client API or manual configuration. Supports intra-tenant masking, strict User ID masking, and phone number overrides. Maps dynamic lookups to a fixed "Life of Mask" timeout. |
| Outgoing Calls | Manages tables for masked outward identities; assigns target caller roles, masked names, and phone assets via bulk import actions. |

---

## 19. Self-Signup

Self-signup allows new organizations or administrators to provision their own contact center environment directly, without requiring manual setup by the platform vendor for each new account. Through a self-service signup flow, an administrator can create an account, configure initial settings, and begin onboarding agents and setting up channels such as voice, chat, and WhatsApp on their own — reducing the time between adoption decision and a working environment, and giving administrators direct control over initial configuration choices.

---

## 20. Platform Navigation and Access

### 20.1 Login and Roles

Users log in with an assigned email address and password (contact an administrator for credentials). **Tenant Admins** have additional menus under Settings and Tenant Admin in the left sidebar. A user's **Role** (e.g., Agent, Supervisor, Admin) controls which menus, features, and settings they can access.

### 20.2 Left Sidebar — Standard Navigation

| Item | Description |
|---|---|
| My Profile | Update personal information, meeting preferences, and login settings |
| Dashboard | Home screen — meeting quick links, ongoing/upcoming/previous meetings, dialpad, missed calls |
| Recordings | Browse, search, download, delete, or export owned or shared recordings |
| Transcriptions | View automatically generated transcripts for recorded sessions |

### 20.3 Quick Action Buttons

| Button | Function |
|---|---|
| Setup Meeting | Launch the meeting creation workflow to schedule a new meeting |
| Join Meeting | Quickly join an existing meeting by entering a Meeting ID |
| Host Instant Meeting | Start an ad-hoc meeting immediately using default settings |

### 20.4 Agent Home

The primary workspace for contact center agents, providing real-time visibility into queued interactions and tools to manage availability/workload.

**Top bar:**

| Control | Function |
|---|---|
| Agent Button | Opens agent-specific controls/settings |
| Dialpad Button | Launches in-app dialpad overlay for outbound voice/video calls |
| Missed Button | Opens Missed Calls modal (calls that rang but weren't answered; refreshable) |

**Queue Counter:** An 'X In Queue' indicator shows the real-time number of customers waiting in the agent's assigned queue.

**Agent Status options** (set via dropdown, determines whether new interactions are routed to the agent): Available, Do Not Disturb, Be Right Back, Offline, Lunch Break, Tea Break, Bio Break, Training Break. (See Section 11 for color coding and lunch-break timing logic.)

**Main navigation menus (sidebar):**

- **Calls:** Recent Calls, Abandoned Calls, Escalated Calls, Customer Calls
- **Chats:** Chats, Customer Chats
- **Dashboards & Reports:** Live Dashboard, Live Chat Dashboard, Reports, Chat Reports
- **Users:** Contacts & Groups, Agents
- **Miscellaneous:** Unified Inbox, Calendar, Daily Updates, Dialpad, Shift Management

### 20.5 Dashboard (Home Screen)

**Quick Info Panel** (copy-to-clipboard enabled):

| Item | Description |
|---|---|
| Default Meeting ID | Personal meeting room identifier |
| Default Meeting Link | Full URL of personal meeting room |
| Default Telephony Meeting ID | Phone-dialable version of the meeting ID |
| Host Code | Private host code, masked by default; reveal/copy via icons |

**Meeting lists:** My Ongoing Meetings (Meeting ID, Telephony Meeting ID, Meeting Name, Start Date/Time, Duration So Far, Actions), My Upcoming Meetings (same fields plus planned Duration and pre-meeting Actions like edit/copy link/start early), My Previous Meetings (Actual Duration, post-meeting Actions like view recording or download transcript).

**Dialpad Modal:** Country Code Selector, Number Input (typed or 12-button keypad), Voice Call Button, Video Call Button.

**Missed Calls Modal:** Opened via the Missed button; shows calls routed but not answered; Refresh button loads the latest.

### 20.6 Setup / Join / Host Instant Meeting Screens

**Setup Meeting:** Meeting ID Type (Use Default / Auto-Generate / Choose Meeting ID), Meeting Name (required, ≤60 chars), Meeting Description (optional, ≤500 chars), Start Date/Time, Duration (hours/minutes, default 1h 0m).

**Join Meeting:** Meeting ID (required dropdown), Start With Video, Include Audio, Mute Audio on Start, Display Name (required), Pass Code (optional), Join Now button.

**Host Instant Meeting:** Use Default Meeting ID, Start With Video, Include Audio, Mute Audio on Start, Start Audio Only Call, Pass Code (optional), Start Now button.

---

## 21. Recordings and Transcriptions (User-Level)

### 21.1 My Recordings Tab

Shows all recordings owned by the user (meetings/calls hosted or saved under their account).

| Control | Function |
|---|---|
| Search / Advanced Search | Filter by name; advanced search adds date range |
| Delete | Permanently remove selected recordings (cannot be undone) |
| Export / Export All | Download selected, or all, recordings |
| Refresh | Reload the recordings list |

**Columns:** Type (Meeting/Webinar), Meeting/Webinar ID, Recording Name, Start Date/Time, File Size, Status (processing/ready/error), Actions (play/download/share/delete).

### 21.2 Shared with Me Tab

Shows recordings shared by other users — viewable/downloadable but not deletable. Columns: Search, Advanced Search, Shared By, Meeting/Webinar ID, Recording Name, Start Date/Time, File Size.

---

## 22. Settings (User-Level)

Settings expand into: **Default Settings** (Meeting, Recording, Transcription, and Miscellaneous Settings — global defaults), **Non Default Settings** (selective overrides using the same options, not enforced globally), and **Call Settings** (incoming call routing, notification preferences, dial modes, flow priorities).

### 22.1 Default Meeting Settings

Applies automatically to every meeting hosted unless overridden. Access: Settings > Default Settings > Meeting Settings.

**Security Settings:**

| Setting | Description |
|---|---|
| Allow Only Logged In Users | Blocks uninvited/anonymous visitors; only signed-in users can join |
| Passcode Protected | Requires a 4–6 character passcode to join |
| Append Password to Meeting Link | Auto-encrypts and appends the passcode to the meeting URL so participants don't need to type it |

> **Note:** At least one of "Allow Only Logged In Users" or "Passcode Protected" must be enabled so meetings are not open to the public.

**Media Settings:**

| Setting | Description |
|---|---|
| Support Audio Over Phone | Allows dial-in audio over telephone/cellular (paid feature) |
| Mute Audio On Start | All participants, including host, start muted |
| Allow Screen Sharing | Share a specific window/browser tab |
| Allow Desktop Sharing | Share the entire desktop (broader than screen sharing) |
| Start With Video | Cameras turned on automatically on join |
| HD Video | Enables 1080p video; requires stable, higher-bandwidth connection |
| Enable Preview Page | Self camera/audio check before entering the meeting room |
| Enable Lobby | Waiting room; host must manually admit each participant |
| Enable High Fidelity Codecs | Uses OPUS as default audio codec for superior audio quality |

**Meeting Haptics (Audio Notifications):** Play Sound On Joining, Play Sound On Leaving.

**Participant Controls:** Allow Participants to Join Before Host; Assign a Participant as Co-Host; Allow Removed Participants to Rejoin; Allow Participants Rename; Allow Participants to Change Profile Pic During Meeting; Moderator Can Lock Meeting.

**Escalation Controls:** Escalation Period (default 24 hours); Escalation Calls Limit Per Escalation Period (default 5 per 24 hours).

### 22.2 Call Settings

Access: Settings > Call Settings. Defines how incoming calls are routed and delivered.

- **Fail-Over Mode:** None, Telephony, VoIP, or Both — fallback/retry mechanism if the user is unreachable.
- **Call Notification Preference:** DVC Client (web/desktop app), Phone Number (registered primary number), Failover Phone Number (backup number; warns if not configured).
- **Dial Flow Settings:** User Dial Preference (lets users override tenant default); Dial Mode (Parallel = all mediums ring simultaneously, answer on whichever responds first); Selected Mediums (active dial mediums, e.g., DCX Web — add/remove via icons; at least one must remain); Preference Order (drag-and-drop priority for sequential mode, attempted top to bottom).
- **Custom MOH Settings:** Plays music to callers on hold; uses a default track unless an administrator uploads a custom audio file or text-to-speech.
- **Flow Preferences & Admin View:** Assign specific call flows and set priority order; shows "No Dial Preferences Found" if none assigned. Admins view/edit dial settings for all users from Tenant Admin > Contact Center Management.

### 22.3 Default Recording Settings

Access: Settings > Default Recording Settings.

**Recording Control:**

| Setting | Description |
|---|---|
| Allow Hosts to Override Tenant-level Settings | Hosts can override non-locked tenant settings |
| Auto Recording | Starts automatically when a session begins |
| Auto Processing | Processes the recording automatically once the session ends |
| Auto Delete Cloud Recordings | Deleted automatically after a set number of days (default 30) |
| Play Audio Prompts (Web / Telephony Users) | Notifies participants that recording has started |
| Require Consent (Web / Telephony Users) | Participants must consent before joining/participating in a recorded session |
| Allow Host and Participants to Record Locally | Permits saving a local copy in addition to the cloud record |

**Recording Content:**

| Mode | Description |
|---|---|
| Audio + Video | Records both audio and all video streams (largest file size, most complete) |
| Audio Only | Records only audio (smaller file, suitable for call logs/voice-only meetings) |
| Hybrid | Audio + video if any participant has video on; falls back to audio-only otherwise |
| Video Recording — Default View | Shared screen alongside active speaker's video |
| Video Recording — Tile View | All participant tiles alongside shared screen (gallery style) |
| Video Recording — Speaker View | Active speaker's video alongside any shared screen |
| Store Chat Messages in a Separate File | Saves in-meeting chat as a separate text file |
| SFU Based Recording | Recording handled by the DolphinCX SFU unit (otherwise default method is used) |

**Access Settings:** Allow Sharing of Recording Links; Allows Agents to View All CC Recordings; Mandate Password for Cloud Recordings; Host Access to Cloud Recording; Host Delete to Cloud Recording.

**Recording Storage:** DolphinCX Storage (default, on DolphinCX infrastructure) or External Custom Storage (administrator-configured external provider).

### 22.4 Default Transcription Settings

Access: Settings > Default Settings > Transcription Settings.

**Transcription Control:** Enable Auto Transcription (generates a text transcript for every recording, processed after the session ends); Allow Hosts/Users to Override tenant- or host-level settings (where not locked); Allow Sharing of Transcription Links; Auto Delete Cloud Transcriptions (default 30 days); Allow Hosts to Download/Delete Transcriptions; Mandate Password for Transcriptions; Allow Agents to View CC Transcriptions.

**Transcription Storage:** DolphinCX Storage (default) or External Custom Storage (mirrors Recording Storage options).

### 22.5 Chat Settings

Access: Settings > Chat Settings.

| Setting | Description |
|---|---|
| Allow "Everyone Messages" | Messages visible to all session attendees |
| Enable Announcements | Admins/moderators can broadcast announcements |
| Allow "One to One" Messages | Private direct messages between participants |
| Allow Agent to Agent Chats | Sub-option permitting private agent-to-agent messaging |
| Agent Chat Session Timeout (secs) | Default 600s; cannot be less than Agent Inactive Timeout |
| Agent Inactive Timeout (secs) | Default 300s; must be between Customer Inactive Timeout and Agent Chat Session Timeout |
| Customer Inactive Timeout (secs) | Default 120s; cannot exceed Agent Inactive Timeout |
| Auto Save Timer (secs) | Default 120s |
| WhatsApp Chat Session Timeout (hours) | Default 24 hours |
| Read Receipts | Tick-mark delivery/read indicators |
| Chat Timeout Template | Default message: "This chat has timed out. Please initiate the chat again if you wish to speak to an agent." |
| WhatsApp Chat | Enables sending messages via WhatsApp from the chat interface |

### 22.6 Telephony Settings

Access: Settings > Default Settings > Miscellaneous Settings (Telephony section).

**Telephony Toggles:** Passcode Protected Telephony; Mask Phone Number In The Participant List; Enable Lock/Unlock Conference (via keypad); Enable Entry Tone; Enable Participant Count (via keypad key sequence); Enable Exit Tone; Dial Out To A Telephone Number (note: disabling this does not disable dial-ins); Enable Claim Host (via key sequence + host code).

**Telephony Countries & Resources:** Select Dial-In Countries; Select Dial-Out Countries; Select Caller ID Numbers; ISD Trunk Preference (e.g., NL_AIRTEL, NL_PBX — move from Available to Selected to activate); STD Trunk Preference (domestic calls, same pool mechanism).

### 22.7 Email and SMS Settings

Access: Settings > Email and SMS Settings.

Both **Email Settings** and **SMS Settings** share the same structure: Enabled (toggle), Endpoint (service URL), Basic Auth Username/Password, and a Settings Header (key-value table for custom HTTP headers; none configured by default).

### 22.8 Feature Settings

Access: Settings > Feature Settings. Controls which buttons/tools/views are available to Moderators and Participants during live sessions.

**Moderator — On-Screen Buttons:** Camera, Microphone, Invite Button, Participant List, Desktop Sharing, Moderator Can See Participants, Polls, Kick Out, Ask to Unmute, Dialpad, Hangup, Full-Screen, Reactions, Chat, Meeting Name, Conference Timer, Notifications Popups, Logo, Call Transfer, Call Hold.

**Moderator — More Options (3-Dot Menu):** Toggle Camera, Mute Everyone, Mute Everyone's Video, Select Background, Closed Captions, Recording, Security Options, Video Quality, Sound Settings, Start Live Streaming With YouTube, Profile Settings, Raise Hand, Shortcuts, Whiteboard, Shared Document, Stats, DVC Invite, Telephony Invite, Moderator Settings.

**Moderator — Views and Audio (at least one view required):** Tile View, Default View, Speaker View, Talk While Muted, No Audio Detected, Noisy Mic Detection.

**Participant — On-Screen Buttons:** Camera, Microphone, Participant List, Desktop Sharing, Invite Button, View Other Participants, Polls, Call Transfer, Hangup, Full-Screen, Reactions, Chat, Meeting Name, Conference Timer, Notifications Popups, Dialpad.

**Participant — 3-Dot Menu & Views:** Toggle Camera, Video Quality, Select Background, Closed Captions, Sound Settings, Stats, Profile Settings, Raise Hand, Shortcuts, Whiteboard, Shared Document, Tile/Default/Speaker Views (at least one required), and haptic fields (Talk While Muted, No Audio Detected, Noisy Mic Detection — mirror moderator alerts).

### 22.9 Contact Center Settings

Access: Settings > Contact Center Settings.

| Setting | Description |
|---|---|
| Maximum No. of Simultaneous Chats Per Agent | Default 4 |
| Post Call Wrapup Duration | Minutes given after a call ends before returning to available (default 5) |
| Auto Available After Wrapup | Auto-returns status to Available when wrapup expires (off by default) |
| Edit Dial Flow Preference | Lets users modify their own dial flow preference (off by default) |
| Redirect To AgentUI | Redirects users to Agent UI after login (off by default) |

### 22.10 Report Settings, AI Tool Settings, and Non Default Settings

- **Report Settings:** Create/manage scheduled reports (Search By Name, Create Report with Name/Description/Type/Frequency, Delete Selected Report).
- **AI Tool Settings:** Lists AI tools/integrations configured for the tenant; shows "No AI Tools Available" as a placeholder until integrations are set up.
- **Non Default Settings:** Mirror Default Settings (Meeting, Recording, Transcription, Miscellaneous) but apply as selective overrides for particular users, groups, or scenarios rather than globally. Two options appear exclusively here: Enable Preview Page and Enable High Fidelity Codecs (Non Default Meeting Settings).

---

## 23. Tenant Administration

### 23.1 Account Info

Access: Tenant Admin > Account Info (admin-only). Controls core tenant configuration.

**Basic Account Info:** Name, Account Number (system-assigned, e.g., TA000020), Domain Prefix (subdomain, e.g., "prachi"), Domain (full platform URL), Welcome Message, Account Type (tier, e.g., "partner"), Maximum Users, Meeting Capacity, Maximum Virtual Agents, Maximum Virtual (Abstract) Users, Max Simultaneous Chats Per Human Agent, Maximum Virtual Agent Chat Sessions, Show Feedback Page After Meeting, End Meeting Redirect URL, Default Country Code (e.g., +91 for India).

**Branding, Support, SSO & Restrictions:** Logo Upload (PNG/JPG), Support Contact Info (name, email, phone), Add Auth Scheme/SSO (e.g., openid_connect with providers like "frappe"), Push Notification Settings (tenant-wide toggle), Allowed Origins List (domains permitted to interact with the tenant's API).

### 23.2 Users & Groups

Access: Tenant Admin > Users & Groups.

**Virtual Users:** Search & Add Virtual User (name, virtual user ID in email format, job description — e.g., IVR handler, bot agent); Virtual User Service Mapping (maps virtual users to services/flows, e.g., link a user ID to telephony and a flow/group); Remove Selected Elements (bulk delete).

**Global Groups:** Organize users into named groups for routing, reporting, and policy. Fields: Group Name/Alias, Note Template (optional, enforces post-interaction note styles for the group), Bulk Group Operations (Add Group, search, edit/delete, bulk removal).

### 23.3 Contact Center Management

Access: Tenant Admin > Contact Center Management. (See also Section 17.3 for Virtual Agent Management details.)

**DID Management:** Maps Direct Inward Dial phone numbers to services, flows, users, or groups for inbound routing; controls starting numbers, ranges, and target IDs.

**CC Flows:** Graphical panels to coordinate call workflows (voice routing engines) and chat routing workflows.

**Document Management:** Upload and map active files into specific folders, making text or files immediately available to automated or human agents during interactions.

**Outbound Campaigns (admin view):** Schedules and reviews campaign operations; filters via duration variables (Week, Month, Year ranges); monitors standalone campaign execution instances.

**Phone Number Lists:** Stores target subscriber contact entries mapped against high-volume outbound campaigns.

### 23.4 Third-Party Integrations and WhatsApp

The Third-Party Systems dashboard handles registration for external CRMs or helpdesk applications. The platform's native WhatsApp integration provides full control over registered numbers, mapping assignments, message templates, and WhatsApp outbound campaigns.

### 23.5 Tenant-Wide Meeting Administration

| Meeting Status | Admin Controls |
|---|---|
| Ongoing Meetings | Real-time inspection of live rooms — Host Name, Login ID, Telephony credentials, elapsed duration; "End Selected Meetings" to instantly terminate rooms |
| Upcoming Meetings | Audit scheduled reservations; cancel/remove selected upcoming meetings |
| Previous Meetings | Historical tracking of completed sessions — host parameters, meeting titles, exact start times |

### 23.6 Recordings & Transcriptions (Tenant-Wide)

The admin view includes extended metadata not exposed to standard users:

- **Recordings Central:** Filter by completion status (Completed, Pending Upload, In Progress) and date; displays file owner's User ID, file sizes, Call Types (inbound, conference), and Agent Types (human vs. virtual agent).
- **Transcriptions Central:** Tracks text records generated across rooms, mapping file sizes, sessions, and human/bot categorization for data governance audits.

### 23.7 Developer Resources

Access: Tenant Admin > Resources.

| Resource | Function |
|---|---|
| API Keys | Secure strings scoped to specific permissions (meeting, recording) for backend server authentication; shown only once at creation |
| SDK Keys | Embed streaming audio/video into standalone customer-facing mobile or web apps |
| Webhooks | Real-time event pushing — links event payloads to destination URLs when system actions complete; includes a test engine |
| Notes & Accounting Templates | Unified documentation structures for customer interactions; manages parameter weights for downstream usage cost calculations |

### 23.8 Plans & Billing

- **Core Plan Specifications:** Subscription boundaries — e.g., Audio Calling core models, usage-based metrics, postpaid/prepaid allocations, concurrent session caps, base rate definitions.
- **Add-On Plan Matrix:** Additional active tenant licenses — Telephony, Video Calling, YouTube Live Streaming, Transcriptions, Audio Conferences, Virtual Agents Calling/Chat capabilities, DID line pricing, storage packages.
- **Payment Info & Invoices:** Corporate identity details (licensed names, GST verification numbers, addresses); interactive billing clearinghouse to monitor invoices, adjust balances, export statement lists.
- **Call Details (CDR):** Granular operational log tracking session initiators, callee arrays, exact connection times, and durations — used for auditing downstream billing formulas.

### 23.9 Tenant Reports

Access: Tenant Admin > Reports.

**Dashboard Reports:** Real-time, auto-refreshing overview — Total Number of Users, Number of Recently Active Users (rolling 3-month window), active-room metrics (Users in Ongoing Meetings, Number of Ongoing Meetings, Average Users per live session).

| Report Category | Metrics |
|---|---|
| General Reports | New users; Session Counts segmented by Platform (Web, Android, iOS) and Device Type (PC, Phone, Tablet) |
| Meeting Reports | Total meeting instances, total elapsed meeting minutes, distinct participant tallies |
| Recording Reports | Recording trends over set intervals or "Until Now"; storage footprints |
| Transcription Reports | Text transcription volume over scheduled windows; tenant filesystem metrics |

---

## 24. Quick Reference

### 24.1 Agent Status Reference

| Status | Operational Impact |
|---|---|
| Available | Ready to receive incoming interactions across active assigned flows |
| Do Not Disturb | Strict immediate routing block on all incoming interactions |
| Temporary Breaks (Be Right Back, Tea Break, Bio Break) | Short absence; interaction delivery suspended |
| Extended Absences (Lunch Break, Training Break) | Structural unavailability flagged to workforce monitors |
| Offline | Agent footprint deactivated; disconnected from routing logic |

### 24.2 Recording Modes Comparison

- **Audio + Video:** Complete multi-stream visual capture (largest file size).
- **Audio Only:** Standard voice tracks, light compliance footprint.
- **Hybrid:** Captures video automatically when streams are active; falls back to voice-only if cameras turn off.

### 24.3 Default vs. Non Default Settings

**Default** settings establish baseline operational behavior across all system communication assets. **Non Default** configurations provide targeted override logic for individual profiles, groups, or situational environments without altering global rules.

### 24.4 Tenant Administration Overview

Centralizes corporate management across: Account Profiles, User Security parameters, Group Routing tables, Virtual Agent conversational workflows, Dial line mask assignments, Webhooks, Developer credentials, and Platform Accounting logs.

### 24.5 Key Reference Parameters

- **Platform Base URL (example tenant):** `https://prachi.signaldesk.dolphinvc.com`
- **Core API Base Endpoint:** `https://meet.dolphincx.com`
- **Legal Documentation:** Privacy Policy and Terms & Conditions are linked in the main profile page application footer.
- **Copyright Statement:** DolphinCX© Copyright 2020 — Powered by Nouveau Labs

---

## 25. DolphinCX (DVC) API Reference

Dolphin Video Conferencing (DVC) provides a REST API for integrating video calling, meeting management, recording, and tenant administration into external applications. All requests/responses use JSON. Authentication uses Bearer tokens (JWT) or Tenant API Keys, depending on endpoint scope.

### 25.1 Authentication and Keys

- **Bearer Token (JWT):** Passed as `Authorization: Bearer <TOKEN>` for standard functional endpoints.
- **Tenant API Key:** Passed via custom header `X-DVC-Tenant-API-Key: <API_KEY_VALUE>` for programmatic administrative use. Permissions can be scoped to `meeting` or `recording` arrays.
- **External Reconcile Engine:** Third-party tokens (e.g., Auth0, Okta) are posted to `/auth/api/v1/reconcile-jwt`, optionally with a target platform role (`tenant_agent`, `tenant_member`, `tenant_operator`), to acquire native operational tokens.

### 25.2 Meeting Creation Options

For `POST /meeting/api/v1/meeting`, core request parameters:

- `meeting_mode`: string (`audio` or `video`)
- `meeting_type`: string (`conference`, `call`, or `stream`)
- `scheduled_meeting_setting`: full object mirroring web interface configuration switches

### 25.3 API Endpoint Inventory

**Tenant API Keys & Auth**

| Method | Endpoint | Description |
|---|---|---|
| POST | `/account/api/v1/tenants/api-key` | Create Tenant API Key |
| GET | `/account/api/v1/tenants/api-key/all` | List all Tenant API Keys |
| DELETE | `/account/api/v1/tenants/api-key` | Delete Tenant API Key |
| POST | `/auth/api/v1/reconcile-jwt` | Exchange 3rd-party JWT for DVC token |
| POST | `/auth/api/v1/refresh-token` | Refresh JWT token |

**Meetings**

| Method | Endpoint | Description |
|---|---|---|
| POST | `/meeting/api/v1/meeting` | Start a new meeting |
| GET | `/meeting/api/v1/join/:meeting_id` | Join an existing meeting |
| POST | `/meeting/api/v1/meeting/call` | Invite users to a call |
| POST | `/account/api/v1/meetings/scheduled` | Create a scheduled meeting |
| GET | `/account/api/v1/meetings/scheduled` | List scheduled meetings |
| PUT | `/account/api/v1/meetings/scheduled` | Update a scheduled meeting |
| DELETE | `/account/api/v1/meetings/scheduled` | Delete a scheduled meeting |

**Recordings**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/account/api/v1/tenants/recording/all` | List all recordings |
| GET | `/account/api/v1/tenants/recording/:id` | Get recording details |
| GET | `/account/api/v1/tenants/recording/:id/download` | Download recording file |
| GET | `/account/api/v1/tenants/recording/:id/transcript/download` | Download transcript |
| DELETE | `/account/api/v1/tenants/recording` | Delete recordings |

**Reports**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/account/api/v1/tenants/reports/general` | General usage report |
| GET | `/account/api/v1/tenants/reports/dashboard` | Dashboard stats |
| GET | `/account/api/v1/tenants/reports/meetings` | Meeting totals report |
| GET | `/account/api/v1/tenants/reports/meetings-per-month` | Monthly meeting counts |
| GET | `/account/api/v1/tenants/reports/recordings/tenant-storage` | Recording storage report |
| GET | `/account/api/v1/tenants/reports/meetings-host-count` | Meetings by host count |
| GET | `/account/api/v1/tenants/reports/meetings-host-duration` | Meetings by host duration |

**Settings**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/account/api/v1/tenants/chat-settings` | Get chat settings |
| PATCH | `/account/api/v1/tenants/chat-settings` | Update chat settings |
| GET | `/account/api/v1/tenants/meeting-settings` | Get meeting settings |
| PATCH | `/account/api/v1/tenants/meeting-settings` | Update meeting settings |
| GET | `/account/api/v1/tenants/recording-settings` | Get recording settings |
| PATCH | `/account/api/v1/tenants/recording-settings` | Update recording settings |
| GET | `/account/api/v1/tenants/telephony-settings` | Get telephony settings |
| PATCH | `/account/api/v1/tenants/telephony-settings` | Update telephony settings |

**Webhooks**

| Method | Endpoint | Description |
|---|---|---|
| POST | `/account/api/v1/tenants/webhook` | Create webhook |
| GET | `/account/api/v1/tenants/webhook/all` | List all webhooks |
| GET | `/account/api/v1/tenants/webhook/:id` | Get webhook details |
| PUT | `/account/api/v1/tenants/webhook/:id` | Update webhook |
| DELETE | `/account/api/v1/tenants/webhook` | Delete webhook(s) |
| GET | `/account/api/v1/tenants/webhook/event/all` | List webhook events |
| GET | `/account/api/v1/tenants/webhook/event/:id` | Get webhook event details |
| POST | `/account/api/v1/tenants/webhook/:id/event/:eid/test` | Test a webhook event |

---

*This document is intended for use as a RAG knowledge base source. Combined and deduplicated from three source documents describing the DolphinCX / SignalDesk contact center platform.*
