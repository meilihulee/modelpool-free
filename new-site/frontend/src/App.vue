<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-gray-100">
    <header class="max-w-7xl mx-auto pt-8 pb-4 px-6">
      <div class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-4xl font-extrabold bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 bg-clip-text text-transparent">
            🚀 LeeHub 资源站
          </h1>
          <p class="mt-2 text-gray-400">AI / 大模型 / VPS / 科技 / 特斯拉 · 实用优先</p>
        </div>
        <div class="hidden md:block text-right text-sm text-gray-500">
          <div>共 {{ resources.length }} 个资源</div>
          <div class="text-cyan-400">{{ categories.length }} 个板块</div>
        </div>
      </div>

      <div class="flex flex-col md:flex-row gap-3 mb-4">
        <input
          v-model="search"
          placeholder="搜索名称、描述或标签..."
          class="flex-1 px-5 py-3 rounded-2xl bg-gray-800/60 border border-gray-600 backdrop-blur focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 outline-none transition"
        />
      </div>

      <div class="flex flex-wrap gap-2">
        <button
          v-for="c in quickFilters"
          :key="c"
          @click="selectedCategory = c"
          :class="[
            'px-3 py-1.5 rounded-lg text-sm border transition',
            selectedCategory === c
              ? 'bg-cyan-600/30 border-cyan-400 text-cyan-200'
              : 'bg-gray-800/40 border-gray-600 text-gray-300 hover:border-cyan-500/60'
          ]"
        >
          {{ c }}
        </button>
      </div>
    </header>

    <main class="max-w-7xl mx-auto px-6 pb-16">
      <div v-if="filtered.length === 0" class="text-center py-20 text-gray-500">
        没有匹配的资源
      </div>

      <template v-else>
        <section class="mb-12" v-if="featured.length">
          <h2 class="text-2xl font-bold mb-6 flex items-center gap-3 text-yellow-300">
            <span>⭐</span>
            <span>热门推荐</span>
            <span class="text-sm font-normal text-gray-500">({{ featured.length }})</span>
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <ResourceCard v-for="r in featured" :key="`f-${r.id}`" :item="r" />
          </div>
        </section>

        <section v-for="group in groupedByCategory" :key="group.category" class="mb-12">
          <h2 class="text-2xl font-bold mb-6 flex items-center gap-3 text-cyan-300">
            <span>📁</span>
            <span>{{ group.category }}</span>
            <span class="text-sm font-normal text-gray-500">({{ group.items.length }})</span>
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <ResourceCard v-for="r in group.items" :key="r.id" :item="r" />
          </div>
        </section>
      </template>
    </main>

    <footer class="border-t border-gray-800 mt-auto">
      <div class="max-w-7xl mx-auto px-6 py-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm">
        <p>© 2026 LeeHub.xyz · 资源导航</p>
        <p class="mt-2 md:mt-0">实用第一，持续更新</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, defineComponent } from 'vue'

const resources = ref([])
const search = ref('')
const selectedCategory = ref('全部')

onMounted(async () => {
  try {
    const res = await fetch('/api/resources')
    if (!res.ok) throw new Error('请求失败: ' + res.status)
    resources.value = await res.json()
  } catch (e) {
    console.error('加载失败:', e)
    resources.value = []
  }
})

const categories = computed(() => {
  const set = new Set(resources.value.map(r => r.category).filter(Boolean))
  return Array.from(set)
})

const quickFilters = computed(() => ['全部', 'AI', '大模型', 'VPS', '科技', '特斯拉', ...categories.value.filter(c => !['AI', '大模型', 'VPS', '科技', '特斯拉'].includes(c))])

const filtered = computed(() => {
  const q = search.value.trim().toLowerCase()
  return resources.value.filter(r => {
    const inCategory = selectedCategory.value === '全部' || r.category === selectedCategory.value
    const matchSearch = !q ||
      r.title?.toLowerCase().includes(q) ||
      r.description?.toLowerCase().includes(q) ||
      (r.tags && r.tags.some(t => t.toLowerCase().includes(q)))
    return inCategory && matchSearch
  })
})

const featured = computed(() => filtered.value.filter(r => r.featured).slice(0, 8))

const groupedByCategory = computed(() => {
  const map = new Map()
  for (const item of filtered.value) {
    const c = item.category || '未分类'
    if (!map.has(c)) map.set(c, [])
    map.get(c).push(item)
  }

  const preferredOrder = ['AI', '大模型', 'VPS', '科技', '特斯拉']
  const result = Array.from(map.entries()).map(([category, items]) => ({ category, items }))

  result.sort((a, b) => {
    const ia = preferredOrder.indexOf(a.category)
    const ib = preferredOrder.indexOf(b.category)
    if (ia !== -1 && ib !== -1) return ia - ib
    if (ia !== -1) return -1
    if (ib !== -1) return 1
    return a.category.localeCompare(b.category, 'zh-CN')
  })

  return result
})

const ResourceCard = defineComponent({
  name: 'ResourceCard',
  props: { item: { type: Object, required: true } },
  template: `
    <div class="p-5 rounded-2xl bg-gray-800/50 border border-gray-700 hover:border-cyan-400/60 hover:shadow-lg hover:shadow-cyan-900/20 transition-all group">
      <div class="flex items-start justify-between mb-3 gap-2">
        <h3 class="font-bold text-white text-lg leading-tight group-hover:text-cyan-300 transition">{{ item.title }}</h3>
        <span class="px-2 py-0.5 text-xs rounded border bg-gray-700/70 text-cyan-200 border-cyan-500/30">{{ item.category }}</span>
      </div>
      <p class="text-gray-400 text-sm mb-4 line-clamp-2">{{ item.description }}</p>
      <div class="flex flex-wrap gap-2 mb-5">
        <span v-for="t in item.tags" :key="t" class="px-2 py-1 text-xs rounded bg-gray-700/60 text-cyan-200">{{ t }}</span>
      </div>
      <div class="flex items-center justify-between">
        <a :href="item.url" target="_blank" class="px-4 py-2 rounded-lg bg-cyan-600/20 hover:bg-cyan-600 text-cyan-300 hover:text-white border border-cyan-500/30 hover:border-cyan-400 transition text-sm font-medium">访问</a>
        <span v-if="item.featured" class="text-xs text-yellow-300">精选</span>
      </div>
    </div>
  `
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
