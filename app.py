from flask import Flask, render_template, abort, send_from_directory
from case_studies import CASE_STUDIES

app = Flask(__name__)

SOCIALS = [
    ("GitHub", "fa-brands fa-github", "https://github.com/muhammadsouman7"),
    ("LinkedIn", "fa-brands fa-linkedin", "https://www.linkedin.com/in/muhammadsouman7/"),
    ("Fiverr", "fiverr-icon", "https://www.fiverr.com/users/muhammadsouman7"),
    ("Upwork", "fa-brands fa-upwork", "https://www.upwork.com/freelancers/~015772745298f0d3b7"),
    ("X", "fa-brands fa-x-twitter", "https://x.com/MuhammadSouman1"),
    ("Instagram", "fa-brands fa-instagram", "https://www.instagram.com/m_souman.07/"),
    ("Facebook", "fa-brands fa-facebook", "https://www.facebook.com/souman.07/"),
]

NAV = [("home", "Home"), ("about", "About"), ("projects", "Projects"),
       ("services", "Services"), ("contact", "Contact")]

# Theme picker options: (key, label, swatch color 1, swatch color 2). Add a matching [data-theme=key] block in style.css.
THEMES = [("mono", "Mono dark", "#f5f5f5", "#555555"), ("paper", "Mono light", "#111111", "#d9d6cf"),
          ("ember", "Ember", "#ffb454", "#ff7a59"), ("emerald", "Emerald", "#86e3a4", "#d4f36b"),
          ("plum", "Plum", "#ff8fb8", "#c99bff"), ("gold", "Gold", "#e6c675", "#c98f4a"),
          ("crimson", "Crimson", "#ff5d6c", "#ff9f7a"), ("sunset", "Sunset", "#ff7a45", "#ff4d8d"),
          ("violet", "Violet", "#b794ff", "#ff9ad5"), ("sage", "Sage", "#b5c99a", "#e0c9a6")]

PROJECTS = [
        dict(title="Shakir Bridal Couture", cat="wordpress", img="shakir-bridal-couture.png", featured=True,
         desc="Custom WordPress and WooCommerce e-commerce store for a bridal couture brand in Islamabad, with custom-built pages and a brand-led design.",
         stack=["WordPress", "WooCommerce", "PHP", "CSS3", "JavaScript"],
         url="https://shakirbridalcouture.com/", cta="Visit site"),
    dict(title="Explainable Deepfake Detection", cat="ai", case="xai-powered-deepfake-video-forensics", img="xai-gallery-img-01.png", featured=True,
        desc="Explainable deepfake detector for images and video built with MTCNN, EfficientNet and Grad-CAM heatmaps that show why a face was flagged.",
         stack=["PyTorch", "EfficientNet", "Grad-CAM", "Flask", "React"],
         url="https://github.com/muhammadsouman7/XAI-Powered-DeepFake-Detection", cta="Source"),
    dict(title="NexSchema: AI Schema Generator", cat="ai", case="nexschema-ai-database-schema-generator", img="nexschema-gallery-img-01.png", featured=True,
             desc="AI database designer built with FastAPI and React: describe an app in plain English and get validated SQL, migration files and an ERD diagram.",
             stack=["FastAPI", "Pydantic", "Groq API", "React", "Mermaid.js"],
             url="https://github.com/muhammadsouman7/NexSchema", cta="Source"),
    dict(title="Tom & Jerry Emotion Detection", cat="ai", case="tom-and-jerry-face-and-emotion-detection", img="cartoon-emotion-detection.png",
         desc="Cartoon emotion detection in PyTorch: a MobileNetV2 transfer learning model that classifies Tom and Jerry faces, served through a Flask web app.",
         stack=["PyTorch", "MobileNetV2", "Flask"],
         url="https://github.com/muhammadsouman7/Cartoon-Face-And-Emotion-Detection", cta="Source"),
    dict(title="Neurosurgeon Dr. Adil Aziz Khan", cat="frontend", img="dr-adil-aziz.png",  featured=True,
             desc="Responsive website for a neurosurgeon with service pages and WhatsApp-integrated appointment booking, built with HTML, CSS, JavaScript and Bootstrap.",
             stack=["HTML5", "CSS3", "JavaScript", "Bootstrap", "WhatsApp API"],
             url="https://neurosurgeondradilazizkhan.com/", cta="Visit site"),
    dict(title="Noor Al-Qalb", cat="ai", case="noor-al-qalb", img="noor-al-qalb.png",
         desc="Emotion-aware NLP web app: a Hugging Face model detects the feeling in your text and returns a matching Quranic verse with translation and audio.",
         stack=["Python", "Flask", "Hugging Face API", "JavaScript"],
         url="https://github.com/muhammadsouman7/noor-al-qalb", cta="Source"),
    dict(title="Personal Book Library", cat="fullstack", img="personal-library.png",
         desc="Flask and SQLite library management system with role-based access: public browsing, member borrowing and returns, and an admin inventory dashboard.",
         stack=["Python", "Flask", "SQLite3", "Bootstrap"],
         url="https://github.com/muhammadsouman7/RhombixTechnologies_Task03", cta="Source"),
    dict(title="Loopify", cat="fullstack", img="loopify.png",
         desc="Flask music player web app with live search and playback controls, built end to end with SQLite and JavaScript as an internship project.",
         stack=["Python", "Flask", "SQLite3", "JavaScript"],
         url="https://github.com/muhammadsouman7/RhombixTechnologies_Task02", cta="Source"),
    dict(title="SoundCatch", cat="fullstack", img="sound-catch.png",
         desc="Ad-free Flask web app that downloads audio from YouTube using yt-dlp, with a clean, simple interface.",
         stack=["Python", "Flask", "yt-dlp"],
         url="https://github.com/muhammadsouman7/Sound-Catch", cta="Source"),
    dict(title="Micro Chatbot", cat="fullstack", img="Micro-ChatBot.png",
         desc="AI chatbot web app with user authentication, built with Flask, SQLite and jQuery and powered by the OpenRouter API.",
         stack=["Python", "Flask", "SQLite3", "OpenRouter API", "jQuery"],
         url="https://github.com/muhammadsouman7/micro-chatbot", cta="Source"),
    dict(title="To-Do List", cat="fullstack", img="to-do-list.png",
         desc="Flask and SQLite to-do list app for adding, editing and completing tasks, built as an internship deliverable.",
         stack=["Python", "Flask", "SQLite3"],
         url="https://github.com/muhammadsouman7/RhombixTechnologies_Task01", cta="Source"),
    dict(title="Neon Login Form", cat="frontend", img="neon-login-form.png",
         desc="Animated neon login and sign-up form in HTML, CSS and jQuery, where the background rotates to reveal the registration form.",
         stack=["HTML5", "CSS3", "jQuery"],
         url="https://muhammadsouman7.github.io/neon-login-form/", cta="Live demo"),
    dict(title="Panda Login Form", cat="frontend", img="panda-login-form.png",
         desc="Interactive panda login form in HTML, CSS and jQuery: the panda covers its eyes when the password field is focused.",
         stack=["HTML5", "CSS3", "jQuery"],
         url="https://muhammadsouman7.github.io/panda-login-form/", cta="Live demo"),
    dict(title="Tirmazi Motors", cat="frontend", img="tirmazi-motors.png",
         desc="Responsive car-rental website built with HTML, CSS and Bootstrap as a university course project.",
         stack=["HTML5", "CSS3", "Bootstrap"],
         url="https://muhammadsouman7.github.io/tirmazi-motors/", cta="Live demo"),
    dict(title="NewAims Pharmaceuticals", cat="frontend", img="newaims-home.png",
         desc="Responsive corporate website for a pharmaceutical company, built with HTML, CSS, JavaScript and Bootstrap in a clean, brand-led layout.",
         stack=["HTML5", "CSS3", "JavaScript", "Bootstrap"],
         url="https://muhammadsouman7.github.io/newaims-pharmaceuticals/", cta="Live demo"),
    dict(title="Abbas Yousaf's Portfolio", cat="frontend", img="abbas-home.png",
         desc="Responsive developer portfolio built with HTML, CSS, JavaScript and Typed.js while mentoring a junior developer through clean, reviewable code.",
         stack=["HTML5", "CSS3", "JavaScript", "Typed.js"],
         url="https://muhammadsouman7.github.io/abbas-yousaf-portfolio/", cta="Live demo"),
]

SERVICES = [
    ("fa-solid fa-layer-group", "Full stack web development", "Custom web applications with Python and Flask, from database schema and REST APIs to a fast, responsive interface.", "wide"),
    ("fa-solid fa-microchip", "AI and machine learning integration", "PyTorch, computer vision and NLP models wired into web products people actually use.", ""),
    ("fa-solid fa-laptop-code", "Responsive frontend development", "Mobile-first, accessible interfaces built with HTML, CSS, JavaScript and Bootstrap.", ""),
    ("fa-solid fa-palette", "UI / UX design", "Interfaces shaped around clarity, hierarchy and how people actually move through them.", ""),
    ("fa-solid fa-database", "Database design", "Sensible relational schemas and efficient queries in MySQL and SQLite.", ""),
    ("fa-brands fa-wordpress", "WordPress and WooCommerce development", "Custom themes, plugins and online stores, plus speed optimization, on sites you can manage yourself.", "wide"),
]

SKILLS = [
    ("Frontend", "fa-solid fa-code", ["HTML5", "CSS3", "JavaScript", "Bootstrap", "jQuery", "React JS"]),
    ("Backend", "fa-solid fa-server", ["Python", "Flask", "REST APIs", "Authentication", "SQLite", "MySQL"]),
    ("AI / ML", "fa-solid fa-brain", ["PyTorch", "Computer Vision", "NLP", "Hugging Face", "Transfer Learning", "Deep Learning", "Machine Learning"]),
    ("WordPress", "fa-brands fa-wordpress", ["Custom themes", "Plugins", "WooCommerce", "Speed optimization"]),
]

PROCESS = [
    ("Understand", "We start with your problem, your users and the constraints before any code is written."),
    ("Design", "Wireframes and a visual direction you can react to early, so there are no surprises later."),
    ("Build", "Clean Flask, WordPress or front-end code, shipped in small steps you can review."),
    ("Ship", "Deployment, handover and support after launch."),
]

TIMELINE = [
    ("2021 - now", "Web development", "More than five years designing and building responsive interfaces with HTML, CSS, JavaScript, Bootstrap, Wordpress, React and Flask."),
    ("Recent", "Full stack development with Python and Flask", "Backend systems, authentication, databases and API integrations, from first commit to launch."),
    ("Ongoing", "B.S. Artificial Intelligence, NUML Islamabad", "8th semester, CGPA 3.64. The theory shapes how I build and evaluate AI features."),
]

SITE = "https://somy.vercel.app"

@app.context_processor
def inject_globals():
    return dict(NAV=NAV, SOCIALS=SOCIALS, THEMES=THEMES, SITE=SITE,
                PROJECT_COUNT=len(PROJECTS),
                FOOTER_CASES=[(slug, cs["title"]) for slug, cs in CASE_STUDIES.items()])

# Page routes
@app.route('/')
def home():
    return render_template('home.html', featured=[p for p in PROJECTS if p.get('featured')],
                           services=SERVICES, skills=SKILLS, process=PROCESS, timeline=TIMELINE)


@app.route('/about')
def about():
    return render_template('about.html', skills=SKILLS, timeline=TIMELINE)


@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)


@app.route('/services')
def services():
    return render_template('services.html', services=SERVICES, process=PROCESS)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/case-study/<slug>')
def case_study(slug):
    cs = CASE_STUDIES.get(slug)
    if not cs:
        abort(404)
    return render_template('case-study.html', cs=cs)

@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html')

# End page routes

# Routes for static files like robots.txt, sitemap.xml, and llms.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt', mimetype='text/plain')


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml', mimetype='application/xml')


@app.route('/llms.txt')
def llms():
    return send_from_directory(app.static_folder, 'llms.txt', mimetype='text/plain; charset=utf-8')

# End routes for static files

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
