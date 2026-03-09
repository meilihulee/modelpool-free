<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-gray-100">
    <!-- 顶部 -->
    <header class="max-w-7xl mx-auto pt-8 pb-4 px-6">
      <div class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-4xl font-extrabold bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 bg-clip-text text-transparent">
            🔗 资源导航
          </h1>
          <p class="mt-2 text-gray-400">发现最好的免费 API 和服务 · 实时更新</p>
        </div>
        <div class="hidden md:block text-right text-sm text-gray-500">
          <div>共 {{ resources.length }} 个资源</div>
          <div class="text-cyan-400">{{ categories.length }} 个分类</div>
        </div>
      </div>

      <!-- 主板块导航 -->
      <div class="flex flex-wrap gap-3 mb-6">
        <button
          v-for="cat in mainCategories"
          :key="cat.id"
          @click="selectedMain = cat.id"
          :class="['px-5 py-2.5 rounded-xl text-sm font-medium transition', selectedMain === cat.id ? 'bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-lg' : 'bg-gray-800/60 text-gray-300 hover:bg-gray-700']"
        >{{ cat.name }}</button>
      </div>

      <!-- 子板块导航（仅 AI 应用场景） -->
      <div v-if="selectedMain === 'ai-apps'" class="flex flex-wrap gap-2 mb-4">
        <button
          v-for="sub in aiSubcategories"
          :key="sub.id"
          @click="selectedSub = sub.id"
          :class="['px-4 py-2 rounded-full text-sm transition', selectedSub === sub.id ? 'bg-purple-600 text-white' : 'bg-gray-800 text-gray-300 hover:bg-gray-700']"
        >{{ sub.name }}</button>
      </div>

      <!-- 搜索 -->
      <div class="flex flex-col md:flex-row gap-4 mb-4">
        <input
          v-model="search"
          placeholder="搜索名称、描述或标签..."
          class="flex-1 px-5 py-3 rounded-2xl bg-gray-800/60 border border-gray-600 backdrop-blur focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 outline-none transition"
        />
      </div>
      <!-- OpenClaw 一键安装包下载 -->
      <section class="mt-2 mb-2">
        <h2 class="text-xl md:text-2xl font-bold text-cyan-300 mb-4">⚡ OpenClaw 一键安装包（新手版）</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="p-5 rounded-2xl bg-gray-800/60 border border-cyan-700/40 hover:border-cyan-400 transition">
            <h3 class="text-lg font-semibold text-white mb-2">🪟 Windows 版</h3>
            <p class="text-sm text-gray-400 mb-4">适合 Windows 10/11，小白一键安装 + 自检 + 修复。</p>
            <div class="flex gap-2">
              <a href="/downloads/openclaw/windows/openclaw-windows-oneclick-kit.zip" class="px-3 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white text-sm">下载安装包</a>
              <a href="/downloads/openclaw/windows/openclaw-windows-oneclick.skill" class="px-3 py-2 rounded-lg border border-cyan-500/40 text-cyan-300 hover:bg-cyan-900/20 text-sm">下载技能包</a>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-gray-800/60 border border-purple-700/40 hover:border-purple-400 transition">
            <h3 class="text-lg font-semibold text-white mb-2">🍎 macOS 版</h3>
            <p class="text-sm text-gray-400 mb-4">适合 Intel / Apple Silicon，终端一键安装与自动修复。</p>
            <div class="flex gap-2">
              <a href="/downloads/openclaw/macos/openclaw-macos-oneclick-kit.zip" class="px-3 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-sm">下载安装包</a>
              <a href="/downloads/openclaw/macos/openclaw-macos-oneclick.skill" class="px-3 py-2 rounded-lg border border-purple-500/40 text-purple-300 hover:bg-purple-900/20 text-sm">下载技能包</a>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-gray-800/60 border border-emerald-700/40 hover:border-emerald-400 transition">
            <h3 class="text-lg font-semibold text-white mb-2">☁️ 云服务器版（Linux）</h3>
            <p class="text-sm text-gray-400 mb-4">支持 Ubuntu / Debian / CentOS / RHEL，一键部署与健康检查。</p>
            <div class="flex gap-2">
              <a href="/downloads/openclaw/linux-server/openclaw-linux-server-oneclick-kit.zip" class="px-3 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-sm">下载安装包</a>
              <a href="/downloads/openclaw/linux-server/openclaw-linux-server-oneclick.skill" class="px-3 py-2 rounded-lg border border-emerald-500/40 text-emerald-300 hover:bg-emerald-900/20 text-sm">下载技能包</a>
            </div>
          </div>
        </div>
      </section>
    </header>

    <!-- 内容 -->
    <main class="max-w-7xl mx-auto px-6 pb-16">
      <div v-if="filtered.length === 0" class="text-center py-20 text-gray-500">
        没有匹配的资源
      </div>
      <!-- 第一板块：按定价分组 -->
      <template v-else-if="selectedMain === 'free-services'">
        <section v-for="group in pricingGroups" :key="group.key" class="mb-12">
          <h2 class="text-2xl font-bold mb-6 flex items-center gap-3" :class="group.titleClass">
            <span>{{ group.icon }}</span>
            <span>{{ group.title }}</span>
            <span class="text-sm font-normal text-gray-500">({{ group.items.length }})</span>
          </h2>
          <div v-if="group.items.length === 0" class="text-gray-500 text-sm">暂无资源</div>
          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <div
              v-for="r in group.items"
              :key="r.id"
              class="p-5 rounded-2xl bg-gray-800/50 border border-gray-700 hover:border-cyan-400/60 hover:shadow-lg hover:shadow-cyan-900/20 transition-all group"
            >
              <div class="flex items-start justify-between mb-3">
                <h3 class="font-bold text-white text-lg leading-tight group-hover:text-cyan-300 transition">{{ r.title }}</h3>
                <span :class="['px-2 py-0.5 text-xs rounded border', usageClass(r.usage_type)]">{{ usageLabel(r.usage_type) }}</span>
              </div>
              <p class="text-gray-400 text-sm mb-4 line-clamp-2">{{ r.description }}</p>
              <div class="flex flex-wrap gap-2 mb-5">
                <span v-for="t in r.tags" :key="t" class="px-2 py-1 text-xs rounded bg-gray-700/60 text-cyan-200">{{ t }}</span>
              </div>
              <div class="flex items-center justify-between">
                <a :href="r.url" target="_blank" class="px-4 py-2 rounded-lg bg-cyan-600/20 hover:bg-cyan-600 text-cyan-300 hover:text-white border border-cyan-500/30 hover:border-cyan-400 transition text-sm font-medium">访问</a>
                <span class="text-xs text-gray-500">{{ pricingLabel(r.pricing) }}</span>
              </div>
            </div>
          </div>
        </section>
      </template>
      <!-- 第二板块：AI 应用场景 -->
      <template v-else-if="selectedMain === 'ai-apps'">
        <div v-if="selectedSub" class="mb-8">
          <h2 class="text-2xl font-bold mb-4 text-purple-400">
            {{ currentSubcategory?.name }}
          </h2>
          <p class="text-gray-400 mb-6">{{ currentSubcategory?.description }}</p>
          <div class="text-center py-20 text-gray-500">
            🚧 正在收集中，敬请期待...
          </div>
        </div>
        <div v-else class="text-center py-20 text-gray-500">
          请选择子分类查看应用案例
        </div>
      </template>
      <!-- 其他板块 -->
      <template v-else>
        <div class="text-center py-20 text-gray-500">
          🚧 建设中...
        </div>
      </template>
    </main>

    <!-- 页脚 -->
    <footer class="border-t border-gray-800 mt-auto">
      <div class="max-w-7xl mx-auto px-6 py-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm">
        <p>© 2025 资源导航 · Vercel + Vue</p>
        <p class="mt-2 md:mt-0">数据来源：公开 API 目录与社区贡献</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const resources = ref([])
const mainCategories = ref([])
const search = ref('')
const selectedMain = ref('free-services')
const selectedSub = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('/api/resources')
    if (!res.ok) throw new Error('请求失败: ' + res.status)
    const data = await res.json()
    resources.value = data
    // 获取主分类列表
    mainCategories.value = [
      { id: 'free-services', name: '免费 API 和服务 · 实时更新' },
      { id: 'ai-apps', name: 'AI 应用场景' }
    ]
  } catch (e) {
    console.error('加载失败:', e)
    resources.value = []
  }
})

// AI 应用场景的子分类（从 categories 数据中提取）
const aiSubcategories = computed(() => {
  const cat = mainCategories.value.find(c => c.id === 'ai-apps')
  return cat?.subcategories || []
})
const currentSubcategory = computed(() => {
  return aiSubcategories.value.find(s => s.id === selectedSub.value)
})

// 过滤资源（只返回当前主板块+子板块匹配的资源）
const filtered = computed(() => {
  let list = resources.value.filter(r => {
    const q = search.value.toLowerCase()
    const matchSearch =
      r.title.toLowerCase().includes(q) ||
      r.description.toLowerCase().includes(q) ||
      (r.tags && r.tags.some(t => t.toLowerCase().includes(q)))
    const matchMain = r.category === selectedMain.value
    // 如果是 ai-apps，还要匹配 subcategory
    let matchSub = true
    if (selectedMain.value === 'ai-apps' && selectedSub.value) {
      matchSub = r.subcategory === selectedSub.value
    } else if (selectedMain.value === 'ai-apps') {
      matchSub = !r.subcategory // 暂不显示未分配子分类的资源
    }
    return matchSearch && matchMain && matchSub
  })
  return list
})

// 第一板块内按定价分组
const pricingGroups = computed(() => {
  if (selectedMain.value !== 'free-services') return []
  const groupFree = filtered.value.filter(r => r.pricing === 'free')
  const groupFreemium = filtered.value.filter(r => r.pricing === 'freemium')
  const groupTrial = filtered.value.filter(r => r.pricing === 'paid-trial')
  return [
    { key: 'free', title: '✅ 完全免费', icon: '✅', items: groupFree, titleClass: 'text-green-400' },
    { key: 'freemium', title: '💰 有免费额度', icon: '💰', items: groupFreemium, titleClass: 'text-blue-400' },
    { key: 'trial', title: '🧪 试用', icon: '🧪', items: groupTrial, titleClass: 'text-yellow-400' }
  ]
})

const usageClass = (usage) => {
  switch (usage) {
    case 'api': return 'bg-purple-500/20 text-purple-400 border-purple-500/30'
    case 'online': return 'bg-orange-500/20 text-orange-400 border-orange-500/30'
    case 'client': return 'bg-teal-500/20 text-teal-400 border-teal-500/30'
    default: return 'bg-gray-700 text-gray-400'
  }
}

const usageLabel = (usage) => {
  switch (usage) {
    case 'api': return 'API调用'
    case 'online': return '在线使用'
    case 'client': return '客户端软件'
    default: return usage || ''
  }
}

const pricingLabel = (pricing) => {
  switch (pricing) {
    case 'free': return 'Gratis'
    case 'freemium': return 'Freemium'
    case 'paid-trial': return '试用'
    default: return 'Info'
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>