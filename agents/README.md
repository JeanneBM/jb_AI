<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/46f9411f-bb92-4fa3-af91-0a105f777758" />

[Trigger: new request]
          |
          v
   +----------------+
   |  ORCHESTRATOR  |
   +----------------+
     |   |     |   \
     |   |     |    \--> [Audit/Logs]
     |   |     |
     |   |     +--> [Rules/Policy Engine] --gates--> (approval needed?)
     |   |
     |   +--> [Agent B: Risk] ----risk+rationale----+
     |
     +--> [Agent A: Facts] ---facts/extracted-------+
                              |
                              v
                     +--------------------+
                     | Agent C: Proposal  |
                     +--------------------+
                              |
                              v
                    (approval needed?) ----yes----> [Human]
                              |                      |
                              no                     v
                              |                 approve/reject
                              v                      |
                     +----------------+               v
                     | ActionExecutor |<-------approve+
                     +----------------+
                              |
                              v
                         [ERP/Payments]
                              |
                              v
                          [Audit/Logs]
