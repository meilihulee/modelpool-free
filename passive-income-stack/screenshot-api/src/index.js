import express from 'express';
import helmet from 'helmet';
import { chromium } from 'playwright';

const app = express();
const PORT = process.env.PORT || 3002;
const API_KEY = process.env.API_KEY || '';

app.use(helmet());

let browser;
async function getBrowser() {
  if (!browser) {
    browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  }
  return browser;
}

function auth(req, res, next) {
  if (!API_KEY) return next();
  const key = req.headers['x-api-key'];
  if (key !== API_KEY) return res.status(401).json({ error: 'unauthorized' });
  next();
}

app.get('/health', (_, res) => res.json({ ok: true, service: 'screenshot-api' }));

app.get('/shot', auth, async (req, res) => {
  const { url, fullPage = 'true', width = '1280', height = '720' } = req.query;
  if (!url) return res.status(400).json({ error: 'url is required' });

  try {
    const b = await getBrowser();
    const page = await b.newPage({ viewport: { width: Number(width), height: Number(height) } });
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
    const buffer = await page.screenshot({
      type: 'jpeg',
      quality: 70,
      fullPage: fullPage === 'true'
    });
    await page.close();

    res.setHeader('Content-Type', 'image/jpeg');
    res.send(buffer);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

process.on('SIGINT', async () => {
  if (browser) await browser.close();
  process.exit(0);
});

app.listen(PORT, () => console.log(`screenshot-api on :${PORT}`));
