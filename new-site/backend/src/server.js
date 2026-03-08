import express from 'express'
import cors from 'cors'
import compression from 'compression'
import { readFile } from 'fs/promises'
import { fileURLToPath } from 'url'
import { dirname, join } from 'path'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const app = express()

app.disable('x-powered-by')
app.set('etag', 'strong')
app.use(cors())
app.use(compression({ level: 6, threshold: 1024 }))
app.use(express.json({ limit: '256kb' }))

// 静态资源（可放图标等）
app.use('/public', express.static(join(__dirname, '../public')))

// 健康检查
app.get('/healthz', (req, res) => {
  res.set('Cache-Control', 'no-store')
  res.json({ ok: true, ts: Date.now() })
})

// GET /api/resources
app.get('/api/resources', async (req, res) => {
  try {
    const dataPath = join(__dirname, 'data', 'resources.json')
    const raw = await readFile(dataPath, 'utf-8')
    const resources = JSON.parse(raw)

    // 读多写少接口，开启短缓存 + 过期回源
    res.set('Cache-Control', 'public, max-age=60, s-maxage=300, stale-while-revalidate=600')
    res.json(resources)
  } catch (err) {
    console.error('读取资源数据失败:', err)
    res.status(500).json({ error: '无法读取资源数据' })
  }
})

const PORT = process.env.PORT || 3000
const server = app.listen(PORT, () => {
  console.log(`🚀 后端运行于 http://localhost:${PORT}`)
})

// 连接复用参数（减少握手开销）
server.keepAliveTimeout = 65000
server.headersTimeout = 66000
