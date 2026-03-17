import express from 'express';
import helmet from 'helmet';
import { JSDOM } from 'jsdom';
import { Readability } from '@mozilla/readability';

const app = express();
const PORT = process.env.PORT || 3001;
const API_KEY = process.env.API_KEY || '';

app.use(helmet());

function auth(req, res, next) {
  if (!API_KEY) return next();
  const key = req.headers['x-api-key'];
  if (key !== API_KEY) return res.status(401).json({ error: 'unauthorized' });
  next();
}

app.get('/health', (_, res) => res.json({ ok: true, service: 'extract-api' }));

app.get('/extract', auth, async (req, res) => {
  const { url } = req.query;
  if (!url) return res.status(400).json({ error: 'url is required' });

  try {
    const controller = new AbortController();
    const t = setTimeout(() => controller.abort(), 15000);
    const r = await fetch(url, {
      signal: controller.signal,
      headers: { 'user-agent': 'Mozilla/5.0 OpenClawExtractor/1.0' }
    });
    clearTimeout(t);

    if (!r.ok) return res.status(400).json({ error: `fetch failed: ${r.status}` });
    const html = await r.text();

    const dom = new JSDOM(html, { url });
    const reader = new Readability(dom.window.document);
    const article = reader.parse();

    if (!article) return res.status(422).json({ error: 'no readable content found' });

    res.json({
      url,
      title: article.title,
      byline: article.byline,
      excerpt: article.excerpt,
      siteName: article.siteName,
      length: article.length,
      contentText: article.textContent,
      contentHtml: article.content
    });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.listen(PORT, () => console.log(`extract-api on :${PORT}`));
