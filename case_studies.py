"""
CASE STUDIES: one dictionary entry per study. The key is the URL slug -> /case-study/<slug>.
Every section is OPTIONAL: delete a key (or leave the list empty) and that section disappears.
To add a study: copy an entry, change the key + content, then set case="<key>" on the matching
project in app.py (PROJECTS). Images live in static/assets/imgs/.
"""

CASE_STUDIES = {
    
    "tom-and-jerry-face-and-emotion-detection": {
        "title": "Tom & Jerry Emotion Detection",
        "seo_title": "Cartoon Face and Emotion Detection with PyTorch | Souman",   # 52 chars
        "seo_desc": "A PyTorch case study on classifying emotions in Tom & Jerry cartoon faces with MobileNetV2 transfer learning, served through a Flask web app.",  # 141 chars
        "keywords": "cartoon emotion detection, PyTorch, MobileNetV2, transfer learning, computer vision, Flask, image classification",
        "tagline": "A PyTorch neural network that recognises emotions on cartoon faces using transfer learning.",
        "category": "AI / Computer vision",
        "role": "Solo developer",
        "timeline": "University / personal project",
        "stack": ["Python", "PyTorch", "MobileNetV2", "Flask", "HTML/CSS/JS"],
        "cover": "cartoon-emotion-detection.png",
        "cover_alt": "Web interface showing a Tom and Jerry cartoon face with its predicted emotion label",
        "links": [("Source code", "https://github.com/muhammadsouman7/Tom-and-Jerry-Emotion-Detection-ANN-Model", "fa-brands fa-github")],

        "problem": [
            "Emotion recognition models are usually trained on real human faces. Cartoon faces have exaggerated features, simplified eyes and mouths, and flat shading, so models built for photographs often misread them.",
            "Collecting a huge cartoon dataset is not realistic for a solo project, so the real question was how well a compact pretrained network can adapt to stylised faces with limited data.",
            "I chose Tom and Jerry because the characters show strong, easy-to-label expressions, which makes them a good test case for cartoon emotion classification.",
        ],
        "goals": [
            "Classify the emotion shown on a cartoon face image",
            "Reuse a pretrained backbone instead of training from scratch",
            "Keep the model small enough to run on modest hardware",
            "Wrap the model in a simple web interface so anyone can test it",
        ],
        "approach": [
            ("Data collection and labelling", "Collected cartoon face images and sorted them into emotion classes. I cleaned out unclear frames and checked the class counts so one emotion did not dominate the training set."),
            ("Transfer learning model", "Used MobileNetV2, pretrained on ImageNet, as a feature extractor. Its general visual features (edges, shapes, textures) carry over to cartoons, so only a new classification head needed to be trained in PyTorch."),
            ("Training and evaluation", "Fine-tuned the model on the labelled set and evaluated it on held-out images it had never seen, to check it generalised instead of memorising the training data."),
            ("Serving through Flask", "Exposed the trained model through a Flask app. A user uploads an image, the backend preprocesses it, runs inference, and returns the predicted emotion to a lightweight HTML/CSS/JS front end."),
        ],
        "features": [
            ("fa-solid fa-image", "Image upload", "Upload a cartoon face and get an emotion prediction in the browser."),
            ("fa-solid fa-microchip", "Transfer learning", "MobileNetV2 backbone with a custom classifier head built in PyTorch."),
            ("fa-solid fa-bolt", "Lightweight", "A small model that runs comfortably on modest hardware, no GPU needed for inference."),
            ("fa-solid fa-layer-group", "Held-out evaluation", "Tested on unseen images to check the model generalises beyond its training data."),
            ("fa-solid fa-globe", "Web interface", "Flask backend with a simple front end, so the model is usable without any code."),
            ("fa-brands fa-github", "Open source", "Full code is public on GitHub for anyone to read, run or extend."),
        ],

        "challenges": [
            ("A small dataset makes overfitting likely.", "Kept the pretrained backbone frozen, trained only the new head, and used augmentation so the model saw more variation."),
            ("Exaggerated cartoon expressions can look similar across classes.", "Cleaned ambiguous frames from the dataset and checked results per emotion rather than trusting one overall score."),
            ("Real-face emotion models do not transfer to cartoons.", "Trained on cartoon-specific images instead of reusing a model built for human faces."),
        ],
        "gallery": [("cartoon-emotion-detection.png", "Prediction screen: an uploaded Tom and Jerry face with the emotion predicted by the model"),
        ("face-emotion-gallery-img-02.png", "Face Detection: an uploaded Tom and Jerry face with the face detected by the model"),
        ("face-emotion-gallery-img-03.png", "Prediction screen: an uploaded Tom and Jerry with the face and emotion predicted by the model")],
        # add more, e.g. ("cartoon-emotion-2.png", "Prediction for a different emotion class"),

        "learned": [
            "Transfer learning lets a small dataset go a long way when the pretrained features are reusable.",
            "Data quality and class balance mattered more than model tweaks.",
            "Serving a model behind a simple Flask route is what turns an experiment into something people can try.",
        ],
        "next": [
            "Add more characters and emotion classes",
            "Add face detection so full scenes can be analysed, not just cropped faces",
            "Show a confidence score with each prediction",
        ],
    },

    "nexschema-ai-database-schema-generator": {
        "title": "NexSchema: AI Database Schema Generator",
        "seo_title": "AI Database Schema Generator with FastAPI & LLMs | Souman",   # 57 chars
        "seo_desc": "A FastAPI and React case study: how NexSchema turns a plain-English app description into validated SQL, migrations and ERD diagrams with an LLM agent.",  # ~156 chars
        "keywords": "AI database schema generator, text to SQL schema, LLM agent, FastAPI, React, Groq, Pydantic, ERD diagram, Mermaid, PostgreSQL, MySQL, database design",
        "tagline": "Describe your app in plain English and get a validated relational schema, migration-ready SQL and an ERD diagram, with every AI answer checked by deterministic rules.",
        "category": "AI / LLM agents",
        "role": "Solo developer",
        "timeline": "Personal project, 2026",
        "stack": ["Python", "FastAPI", "Pydantic", "Groq API", "React", "Vite", "Tailwind CSS", "Mermaid.js"],
        "cover": "nexschema-gallery-img-01.png",
        "cover_alt": "NexSchema prompt screen where a user describes an application in plain English and picks PostgreSQL or MySQL",
        "links": [("Source code", "https://github.com/muhammadsouman7/NexSchema", "fa-brands fa-github")],

        "problem": [
            "Designing a database starts with the same slow steps every time: listing entities, choosing types, wiring foreign keys, adding junction tables, then writing the SQL by hand. Mistakes here are expensive because they spread into every layer built on top.",
            "Asking a general chatbot for a schema is fast, but the answer is unreliable. It can reference tables that do not exist, skip primary keys, or return SQL that fails on the first run, and nothing checks it.",
            "I wanted to see if an LLM could be used only for understanding the description, while ordinary code builds, checks and corrects the schema. That split is the core idea behind NexSchema.",
        ],
        "goals": [
            "Turn a plain-English app description into a relational schema",
            "Generate runnable SQL for PostgreSQL and MySQL, split into migration files",
            "Produce an ERD diagram that can be downloaded",
            "Validate every AI result with deterministic rules before showing it",
            "Be upfront about the assumptions and ambiguities the AI found in the prompt",
        ],
        "approach": [
            ("Prompt guard", "Before any AI call, a rule-based validator rejects clearly off-topic input such as maths questions, jokes or greetings, and returns a clear message. This saves API calls and keeps the model focused on database design."),
            ("Two-phase LLM extraction", "The first call extracts tables and columns as strict JSON. A second call extracts relationships using only the table names from phase one. Splitting the work keeps each response small and avoids truncated output."),
            ("Intermediate representation", "AI output is parsed into Pydantic models and transformed into a database-neutral schema. A relationship engine then creates foreign keys and junction tables for one-to-many, one-to-one and many-to-many links."),
            ("Validate and refine loop", "A validator checks for duplicate tables, missing or nullable primary keys, broken foreign keys, duplicate columns, circular references and missing audit columns. Errors are fed back to the model as a correction prompt, up to 12 steps."),
            ("Generators and dashboard", "Generators render dialect-specific SQL in dependency order, plus Mermaid and PlantUML ERDs. A React dashboard shows tables, SQL with copy and download, and the rendered ERD, with SVG and PNG export."),
        ],
        "features": [
            ("fa-solid fa-wand-magic-sparkles", "Plain-English input", "Describe an app and get tables, columns, keys and relationships back."),
            ("fa-solid fa-shield-halved", "Deterministic validation", "Rule-based checks catch broken keys and duplicates instead of trusting the model."),
            ("fa-solid fa-rotate", "Self-correcting agent", "Validation errors are sent back to the model automatically until the schema passes."),
            ("fa-solid fa-database", "PostgreSQL and MySQL", "Dialect-aware SQL with migration files for tables and indexes."),
            ("fa-solid fa-diagram-project", "ERD diagrams", "Mermaid diagrams rendered in the browser, exportable as .mmd, SVG or PNG."),
            ("fa-solid fa-circle-info", "Assumptions shown", "Ambiguities, assumptions and warnings are listed next to the result."),
        ],

        "challenges": [
            ("LLM output can be invalid or cut off mid-JSON.", "Used JSON response mode, a token-limit check on every call, per-call retries that feed the error back to the model, and a two-phase prompt to keep responses short."),
            ("The model sometimes references tables it never defined.", "Added a validator that checks every foreign key target and sends the exact error back to the model as a correction prompt."),
            ("Many-to-many relationships need junction tables.", "Built a relationship inference engine that creates the junction table and its two foreign keys deterministically instead of relying on the model."),
            ("Tables must be created in dependency order.", "Sorted tables topologically before generating SQL so foreign keys never point to a table that does not exist yet."),
            ("Provider rate limits and off-topic prompts waste requests.", "Handled rate limits with retry-after backoff and a clear 429 message, and added a prompt guard that blocks unrelated input before any API call."),
        ],
        "gallery": [
            ("nexschema-gallery-img-01.png", "Prompt screen where the user describes an application and selects PostgreSQL or MySQL"),
            ("nexschema-gallery-img-02.png", "Generated tables view with column types, keys and nullability for each table"),
            ("nexschema-gallery-img-03.png", "Generated SQL migration files with syntax highlighting, copy and download"),
            ("nexschema-gallery-img-04.png", "Generated ERD diagram showing tables and their relationships"),
        ],

        "learned": [
            "Use the LLM for understanding and let plain code do the checking. A validator that talks back to the model is more reliable than a longer prompt.",
            "Smaller, separate LLM calls (tables first, then relationships) fail less often than one huge request.",
            "Showing assumptions and warnings builds more trust than presenting the output as always correct.",
        ],
        "next": [
            "Add SQLite output (the API already accepts it, the SQL generator does not yet)",
            "Let users edit the schema and regenerate only the changed parts",
            "Add automated tests for the validator and relationship engine",
            "Export Prisma, SQLAlchemy or Django model code",
        ],
    },

    "noor-al-qalb": {
        "title": "Noor Al-Qalb",
        "seo_title": "Emotion-Based Quran Verse Finder with Flask & NLP | Souman",   # 58 chars
        "seo_desc": "A Flask and Hugging Face case study: how Noor Al-Qalb detects emotion in text with DistilBERT and returns a Quranic verse with translation and audio.",  # ~152 chars
        "keywords": "emotion detection, NLP, Hugging Face, DistilBERT, Flask, Quran verses, sentiment analysis, text classification, Vercel",
        "tagline": "A Flask web app that reads how you feel, detects the emotion with an NLP model, and answers with a Quranic verse, its translation and audio recitation.",
        "category": "AI / NLP",
        "role": "Solo developer",
        "timeline": "Personal project",
        "stack": ["Python", "Flask", "Hugging Face Inference API", "DistilBERT", "JavaScript", "Bootstrap", "Vercel"],
        "cover": "noor-al-qalb.png",
        "cover_alt": "Noor Al-Qalb web app showing a Quranic verse in Arabic with its translation and audio play button",
        "links": [("Source code", "https://github.com/muhammadsouman7/noor-al-qalb", "fa-brands fa-github")],

        "problem": [
            "When people feel anxious, sad or grateful, they often look for words that fit the moment. Finding a relevant passage in a large text takes time and knowing where to look.",
            "I wanted to see whether a text-emotion model could do that matching: the user describes a feeling in their own words, and the app responds with a fitting verse in a calm, readable way.",
            "Because this is religious content, accuracy and humility mattered more than cleverness. The app uses AI only to pick the emotion; the verses themselves are a fixed, curated set, not generated text.",
        ],
        "goals": [
            "Detect the emotion in free-form text a user types",
            "Return a relevant verse with its translation and a short explanatory note",
            "Let the user listen to the recitation without leaving the page",
            "Keep the interface calm, fast and usable on a phone",
            "Be upfront that the model can misread tone",
        ],
        "approach": [
            ("Emotion detection", "The Flask backend sends the user's text to a pretrained DistilBERT emotion model through the Hugging Face Inference API, receives a score for each emotion, and keeps the highest one."),
            ("Curated verse set", "A JSON file maps six emotions (sadness, joy, love, anger, fear, surprise) to five verses each. Every entry holds the Arabic text, translation, topic, a tafsir source and a short note for the reader."),
            ("Verse display and audio", "The front end picks a verse for the detected emotion and renders it. The play button fetches the recitation from the Al-Quran Cloud API, and multi-ayah ranges play one after another."),
            ("Deployment", "The Flask app is deployed on Vercel, while the heavy model runs on Hugging Face, so the app stays light and easy to host."),
        ],
        "features": [
            ("fa-solid fa-face-smile", "Emotion detection", "Classifies the feeling behind a sentence into one of six emotions."),
            ("fa-solid fa-book-quran", "Verse and translation", "Shows the Arabic verse, its English translation and a short note."),
            ("fa-solid fa-volume-high", "Audio recitation", "Plays the verse in the browser, including multi-verse ranges."),
            ("fa-solid fa-shield-halved", "Fallback handling", "Falls back to a safe default emotion if the model returns a label with no verses."),
            ("fa-solid fa-lock", "Server-side API key", "The Hugging Face token stays on the backend and is never exposed to the browser."),
            ("fa-solid fa-mobile-screen", "Responsive layout", "A clean Bootstrap interface that works on phones and desktops."),
        ],

        "challenges": [
            ("A pretrained emotion model can misread short or ambiguous text.", "Added an honest note on the welcome screen telling users the prediction may be wrong, so the app is a tool for reflection, not an authority."),
            ("The model can return an emotion that has no verses in the dataset.", "Added a fallback in the backend so the user always gets a verse instead of an empty result."),
            ("Some verses are ranges, and the audio API plays one ayah at a time.", "Split ranges like 2:255-257 into single ayahs and queued them, playing the next recitation when the previous one ends."),
            ("The model is too heavy to run inside a serverless deployment.", "Kept inference on Hugging Face's API and deployed only the lightweight Flask app, keeping the API token server-side."),
        ],
        "gallery": [
            ("noor-al-qalb.png", "Noor Al-Qalb verse result with Arabic text, translation and audio button"),
        ],

        "learned": [
            "Using AI for one narrow job (classification) and a curated dataset for the sensitive content keeps the output trustworthy.",
            "A fallback for every external call matters when your app depends on two third-party APIs.",
            "Being clear about a model's limits builds more trust than hiding them.",
        ],
        "next": [
            "Add more verses per emotion so results feel less repetitive",
            "Support more emotions and show the model's confidence",
            "Add Arabic and Urdu input, since the current model handles English text",
            "Let users save favourite verses",
        ],
    },
    "xai-powered-deepfake-video-forensics": {
        "title": "Explainable Deepfake Detection",
        "seo_title": "Explainable Deepfake Detection with Grad-CAM | Souman",   # 53 chars
        "seo_desc": "A PyTorch case study on detecting deepfake images and videos with MTCNN, EfficientNet and Grad-CAM heatmaps, served via a Flask API and React dashboard.",  # ~152 chars
        "keywords": "explainable AI, deepfake detection, Grad-CAM, EfficientNet, MTCNN, PyTorch, computer vision, Flask, React, final year project",
        "tagline": "A deepfake detector that doesn't just say real or fake, it highlights the face regions behind its verdict.",
        "category": "AI / Explainable computer vision",
        "role": "Co-developer (3-person team)",   # adjust to your exact part, e.g. "Model + backend"
        "timeline": "Final year project, NUML, 2025",
        "stack": ["Python", "PyTorch", "EfficientNet", "MTCNN", "Grad-CAM", "Flask", "React"],
        "cover": "xai-gallery-img-01.png",
        "cover_alt": "Deepfake forensics dashboard showing a verdict and a Grad-CAM heatmap over a detected face",
        "links": [("Source code", "https://github.com/muhammadsouman7/XAI-Powered-DeepFake-Detection", "fa-brands fa-github")],

        "problem": [
            "Most deepfake detectors return a single probability and nothing else. That is hard to trust, and harder to defend when a journalist, analyst or moderator has to justify a decision.",
            "For our final year project, my team set out to build a detector whose reasoning can be inspected: if the model calls a face fake, it should also show which parts of the face drove that call.",
            "The challenge was keeping the accuracy of a modern CNN classifier while adding an explanation layer a human reviewer can agree or disagree with.",
        ],
        "goals": [
            "Classify uploaded images and videos as real or fake",
            "Show a visual explanation (heatmap) alongside every verdict",
            "Handle video by sampling frames instead of processing every one",
            "Deliver it through a dashboard that feels like an investigation tool, not a demo",
        ],
        "approach": [
            ("Face detection", "MTCNN finds and crops the most prominent face from an image, or from up to 15 evenly spaced frames of a video, resized to 224x224 for the classifier."),
            ("Classification", "A fine-tuned EfficientNet with a custom classification head scores each face crop. Scores are averaged across frames to give one video-level verdict."),
            ("Explainability", "Grad-CAM hooks into the last convolutional block and produces a heatmap over the highest-confidence face, showing which regions influenced the prediction."),
            ("API and dashboard", "A Flask endpoint runs the pipeline and returns the verdict and heatmap to a React dashboard with drag-and-drop upload and live pipeline-stage feedback."),
        ],
        "features": [
            ("fa-solid fa-film", "Image and video input", "Upload a photo or a short clip and get a single verdict."),
            ("fa-solid fa-fire", "Grad-CAM heatmaps", "See the facial regions that pushed the model toward real or fake."),
            ("fa-solid fa-face-viewfinder", "Face-focused pipeline", "MTCNN crops keep the classifier looking at the face, not the background."),
            ("fa-solid fa-chart-simple", "Frame-level aggregation", "Averaging over sampled frames makes video verdicts less fragile than a single frame."),
            ("fa-solid fa-gauge-high", "CPU / GPU fallback", "Runs on CUDA when available and falls back to CPU automatically."),
            ("fa-solid fa-window-maximize", "Forensic dashboard", "A React interface that walks the reviewer through each stage before showing the result."),
        ],

        "challenges": [
            ("A bare confidence score is not evidence a reviewer can question.", "Added Grad-CAM so every verdict ships with a heatmap that can be checked visually."),
            ("Videos are too long to analyse frame by frame.", "Sampled up to 15 evenly spaced frames, which keeps coverage proportional while keeping inference fast."),
            ("Inconsistent face crops hurt classifier input quality.", "Used MTCNN with a margin around the face so every crop is aligned and sized the same way."),
            ("Temporal analysis is more than a heuristic.", "The dashboard's temporal score is currently derived from the variance of per-frame predictions, and I label it as a proxy rather than a dedicated sequence model."),
        ],
        "gallery": [
            ("xai-gallery-img-01.png", "Upload screen of the deepfake forensics dashboard"),
            ("xai-gallery-img-02.png", "Pipeline stages running during analysis of an uploaded video"),
            ("xai-gallery-img-03.png", "Verdict view with a Grad-CAM heatmap over the detected face"),
        ],

        "learned": [
            "Explainability changes how people use a model: a heatmap turns a number into something you can discuss.",
            "Splitting the system into detection, classification and explanation made each stage easier to test and debug.",
            "Being upfront about what a heuristic score can and cannot show matters as much as the model itself.",
        ],
        "next": [
            "Replace the variance-based temporal score with a real sequence model (LSTM or 3D-CNN)",
            "Benchmark accuracy on public datasets such as FaceForensics++ or Celeb-DF",
            "Analyse every face in multi-person videos, not just the most prominent one",
        ],
    },
    
}
