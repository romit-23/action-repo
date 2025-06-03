# Action Repo – GitHub Webhook Demo Repository

This is a demo repository created to test and trigger GitHub webhook events as part of a developer assessment task.

It contains basic placeholder content and sample Git activity (such as commits, pull requests, and merges) to simulate real repository behavior. These actions are used to send event payloads to a Flask-based GitHub webhook receiver application built as part of the assessment.


🚀 **How it Works**:
Whenever a push, pull request, or merge is performed on this repository, a GitHub webhook sends the event data to the configured receiver endpoint. This data is then:
- Parsed by the Flask application
- Stored in MongoDB
- Displayed in a real-time UI that updates every 15 seconds

🔗 **Webhook Receiver Repository**:
The actual application that handles the webhook events is hosted here:  
👉 [webhook-repo](https://github.com/romit-23/webhook-repo)

Please visit that repository for:
- Full implementation details
- MongoDB schema
- Webhook endpoint documentation
- Live demo instructions and UI features

---

📄 **Note**:
This repository is intentionally minimal and only serves as the GitHub-side trigger for the webhook system. All core logic and functionality reside in the `webhook-repo`.

