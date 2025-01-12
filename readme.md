# float



**float** is a latent-thought-based learning agent designed to run on locally managed hardware with a strong emphasis on privacy. It specializes in efficient latent modeling and is augmented by external systems to enhance its capabilities.



### Architecture



- **Language Models & APIs:**

  - **Primary Models:** Mistral Language Model, Google Pali+/Gemma, OpenAI API

  - **Computer Vision:** OpenCV

- **Data Stores:**

  - **Vector & Graph Databases:** For efficient, accurate, and relevant world modeling.

- **Tool Calling:**

  - **ETL, Data Augmentation, Generation Augmentation**

  - **Training and Unit Testing Pipelines:** For predictive modeling or reinforcement learning.

- **Data Management:**

  - Designed to work with sparse data, dynamically compressing and expanding to fit changing schemas.

- **Error Correction:**

  - Maintains and propagates confidence of observations for quick updates and data filtering/conversion.

- **Modularity:**

  - Internal models and features are replaceable to ensure longevity through hardware/software updates and internal epochs.

- **Reasoning:**

  - Utilizes special tokens to reason within hidden layers, enhancing efficiency.

  - Implements a patience input parameter to limit the use of reasoning tokens.

- **Observational Capabilities:**

  - Learns about given topics, the user, and the world to build, augment, or correct world models.

- **Proactive and Agentic:**

  - Works asynchronously and agentically to schedule and complete tasks, interact with users, and update understandings.

  - Capable of recalling internal modules finitely.

- **Privacy:**

  - Locally managed with encrypted memories and masked API calls to handle sensitive information securely.



### Specifications



- **Hardware:**

  - GPUs: NVIDIA RTX 4070 -> RTX 5090 (12-32GB VRAM) for language and reinforcement learning models.

  - **External APIs:** Google and OpenAI APIs for complex tasks.

- **Memory & Storage:**

  - NAS backup and substantial storage, especially as agentic observation scales.

- **Cloud Integration:**

  - Google Cloud integration for scalability.

  - Containers and cloud GPU deployment abstracted as tools.

- **Embeddings:**

  - Sentence Transformers or similar models.

- **Tokenizer:**

  - Custom tokenizer with special tokens (`<bot>`, `<eot>`, `<tool>`) inspired by Meta Coconut.

  - Interest in patch-based systems like Meta BLT.

- **Model Interaction:**

  - Extra considerations for interacting with model hidden layers and tokenization processes.

- **Models:**

  - Multi-modal and language-specific models are desirable.

  - Leverages prompt chains with specific system prompts to pass information as needed.

- **Database:**

  - Options: PostgreSQL + ChromaDB or SQLite + Weaviate for specific functions.

- **Data Handling:**

  - **Tabular Data:** Full chat history for direct access, quick search + embedding capabilities.

  - **Embedded Memories:** Proactively embed pertinent details for future retrieval.

  - **Learned Knowledge:** Embed knowledge in separate retrievable tables.

- **Consistency:**

  - Utilizes timestamps, data expiration, confidence, and bias estimations to support the learning function.

- **Graph Networks:**

  - Entries are nodes by default, with optional edges to represent relationships.

- **Tool Collection:**

  - Defined within a `tools` directory, comprising Python functions and their input schemas.

  - Basic tools for ETL, CV, external model requests, and web interactions.

- **Tool Permissions:**

  - Some tools require user approval, pausing the chain until input is received.

- **Backend:**

  - **Framework:** FastAPI for asynchronous features, scalability, and comprehensive documentation.

  - **Task Management:** Celery for asynchronous tool execution pipelines.

  - **Schema Validation:** Pydantic.

  - **Visualization Tools:** ChromaViewer, NetworkX, PyVis, and Pandas.

  - **Testing:** Pytest for structure validation before updates.

  - **Model Serving:** LMStudio (with KoboldCPP and Ollama as alternatives) for local models.

- **Frontend:**

  - **Framework:** Vue.js, with potential transition to React for more complex and modular interfaces.

  - **UI Features:**

    - Dynamic presentation of thoughts/tools/approvals in a right sidebar.

    - Selectable messages from Float to view processing details.

    - Persistent streaming box at the bottom to display recent thoughts.

    - Use of special tokens to determine breakpoints.

  - **Visualizations Tab:**

    - Navigation away from chat to explore the knowledge base, possibly with chat persisting in a sidebar.

    - Interactive, dynamic views and mapping using D3.js and/or Plotly Dash.

- **Security:**

  - **Encryption:** AES-256

  - **Key Management:** Google Cloud KMS for key storage.

  - **Data Integrity:** SHA-256 hashing.
