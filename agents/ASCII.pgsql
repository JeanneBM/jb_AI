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
