# 📝 AI-Powered Blog Post Generator

This project is a Flask-based backend that generates SEO-optimized blog posts using Cohere's Command R+ model. Given a keyword, it performs lightweight SEO analysis and uses AI to draft blog content with real-looking affiliate links. The app also supports daily automated blog generation via a built-in scheduler.

---

## 🚀 Features

- 🔍 Fetches mock SEO metrics (search volume, keyword difficulty, CPC)
- 🧠 Uses Cohere LLM to generate blog posts in Markdown format
- 🔗 Automatically includes affiliate-style links within the post
- 📦 Saves generated posts to a local `/generated` folder
- ⏱ Includes a daily scheduled job (via APScheduler)
- 🌐 Exposes a `/generate` API endpoint

---

## 📁 Project Structure

```
ai-blog-generator/
├── app.py                  # Flask app + scheduled job
├── ai_generator.py         # LLM-based blog generation
├── seo_fetcher.py          # Mock SEO data
├── requirements.txt        # Dependencies
├── .env                    # API key (not committed)
├── generated/              # Saved blog posts
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/anshramanath/ai-blog-generator-interview-ansh.git
   cd ai-blog-generator-interview-ansh
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key**:
   Create a `.env` file with your Cohere API key:
   ```
   COHERE_API_KEY=your_api_key_here
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

   This will:
   - Start the Flask server on `http://127.0.0.1:5000`
   - Trigger the scheduled job 10 seconds after launch, then once every day

---

## 🔗 Usage

**Generate a post manually**:
```http
GET /generate?keyword=wireless-earbuds
```

- Keywords must match one of the supported slugs:
  - `wireless-earbuds`
  - `protein-powder`
  - `best-laptops`
  - `budget-travel-tips`
  - `freelance-web-developer`

If the keyword is not supported, you'll get:
```json
{ "error": "Keyword 'xyz' is not supported." }
```

---

## 🗃 Example Output

After hitting `/generate`, you’ll find a markdown file saved at:
```
/generated/your-keyword_YYYY-MM-DD.md
```

It will include:
- A full blog post in markdown
- SEO stats
- Context-aware affiliate links

---

## 🧠 Tech Stack

- Python 3.10+
- Flask
- APScheduler
- Cohere Command R (via `cohere` SDK)
- dotenv