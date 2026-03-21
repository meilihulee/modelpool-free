<template>
  <div class="min-h-screen bg-zinc-950 text-zinc-100 antialiased relative overflow-hidden">
    <div class="fixed inset-0 pointer-events-none overflow-hidden">
      <div class="orb orb-primary animate-orb-1 w-96 h-96 -top-48 -left-48 opacity-30"></div>
      <div class="orb orb-cyan animate-orb-2 w-80 h-80 top-1/4 right-0 opacity-25"></div>
      <div class="orb orb-purple animate-orb-3 w-72 h-72 bottom-0 left-1/3 opacity-20"></div>
      <div class="orb orb-pink w-64 h-64 top-1/2 right-1/4 animate-orb-1 opacity-15"></div>
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_transparent_0%,_rgba(10,10,15,0.8)_70%)]"></div>
      <div class="absolute inset-0" style="background-image: radial-gradient(rgba(99,102,241,0.03) 1px, transparent 1px); background-size: 32px 32px;"></div>
    </div>

    <div class="relative z-10">
      <header class="relative border-b border-white/[0.06]">
        <div class="absolute inset-0 bg-gradient-to-b from-primary-500/5 via-transparent to-transparent pointer-events-none"></div>
        <div class="relative mx-auto max-w-7xl px-5 py-10 md:px-8 md:py-14">
          <div class="flex items-center gap-3 mb-2 animate-fade-in-up">
            <div class="flex items-center gap-2 rounded-full border border-primary-500/20 bg-primary-500/10 px-4 py-1.5 backdrop-blur-sm">
              <span class="relative flex h-2 w-2">
                <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-primary-400 opacity-75"></span>
                <span class="relative inline-flex h-2 w-2 rounded-full bg-primary-400"></span>
              </span>
              <span class="text-xs font-medium tracking-wide text-primary-300">LeeHub · 精选 AI 工具导航</span>
            </div>
          </div>

          <h1 class="mt-6 text-4xl font-bold tracking-tight md:text-5xl lg:text-6xl animate-fade-in-up animate-delay-100">
            <span class="text-zinc-100">找到你真正会用上的</span>
            <br />
            <span class="gradient-text glow-text">AI 工具</span>
          </h1>
          <p class="mt-5 max-w-2xl text-sm leading-relaxed text-zinc-400 md:text-base animate-fade-in-up animate-delay-200">
            收录优质的 AI 工具与资源，覆盖开发、设计、效率等场景。已收录
            <span class="font-semibold text-zinc-200">{{ resources.length }}</span>
            个工具，支持关键词、分类与标签快速筛选。
          </p>

          <div class="mt-8 grid gap-4 sm:grid-cols-3 animate-fade-in-up animate-delay-300">
            <div class="stat-card group p-5 hover:shadow-glow">
              <div class="flex items-center gap-3">
                <div class="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-primary-500/20 to-primary-600/10 border border-primary-500/20">
                  <svg class="h-5 w-5 text-primary-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-medium uppercase tracking-widest text-zinc-500">精选工具</p>
                  <p class="mt-0.5 text-2xl font-semibold text-zinc-100">{{ featuredResources.length }} <span class="text-sm font-normal text-zinc-500">个</span></p>
                </div>
              </div>
            </div>
            <div class="stat-card group p-5 hover:shadow-glow-cyan">
              <div class="flex items-center gap-3">
                <div class="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-accent-cyan/20 to-accent-cyan/5 border border-accent-cyan/20">
                  <svg class="h-5 w-5 text-accent-cyan" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-medium uppercase tracking-widest text-zinc-500">工具分类</p>
                  <p class="mt-0.5 text-2xl font-semibold text-zinc-100">{{ categories.length }} <span class="text-sm font-normal text-zinc-500">个</span></p>
                </div>
              </div>
            </div>
            <div class="stat-card group p-5 hover:shadow-glow-purple">
              <div class="flex items-center gap-3">
                <div class="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-accent-purple/20 to-accent-purple/5 border border-accent-purple/20">
                  <svg class="h-5 w-5 text-accent-purple" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-medium uppercase tracking-widest text-zinc-500">有效资源</p>
                  <p class="mt-0.5 text-2xl font-semibold text-zinc-100">{{ validResources.length }} <span class="text-sm font-normal text-zinc-500">个</span></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main class="mx-auto max-w-7xl px-5 py-8 md:px-8">
        <section class="glass-panel p-5 mb-8 animate-fade-in-up animate-delay-400">
          <div class="flex flex-col gap-4 sm:flex-row sm:items-center">
            <div class="relative flex-1">
              <div class="absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none">
                <svg class="h-5 w-5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
                <input
                v-model="search"
                type="text"
                placeholder="搜索工具名称、描述或标签"
                class="w-full rounded-xl border border-white/[0.06] bg-white/[0.02] py-3.5 pl-12 pr-4 text-sm text-zinc-100 placeholder-zinc-500 outline-none transition-all duration-300 input-glow focus:border-primary-500/50 focus:bg-white/[0.04]"
              />
            </div>
            <button
              v-if="search || selectedCategory !== '全部'"
              type="button"
              class="flex items-center justify-center gap-2 rounded-xl border border-red-500/20 bg-red-500/5 px-5 py-3 text-sm font-medium text-red-400 transition-all duration-200 hover:border-red-500/40 hover:bg-red-500/10 hover:shadow-[0_0_20px_-5px_rgba(239,68,68,0.3)]"
              @click="resetFilters"
            >
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
              重置
            </button>
          </div>

          <div class="mt-5 flex flex-wrap gap-2.5">
            <button
              v-for="cat in ['全部', ...categories]"
              :key="cat"
              type="button"
              :class="chipClass(selectedCategory === cat)"
              @click="selectedCategory = cat"
            >
              {{ cat }}
            </button>
          </div>
        </section>

        <section v-if="featuredResources.length" class="mb-10">
          <div class="mb-6 flex items-center gap-4">
            <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-amber-500/20 to-orange-500/10 border border-amber-500/20 shadow-[0_0_20px_-5px_rgba(245,158,11,0.3)]">
              <svg class="h-5 w-5 text-amber-400" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
              </svg>
            </div>
            <div>
              <h2 class="text-xl font-semibold text-zinc-100">编辑精选</h2>
              <p class="text-xs text-zinc-500">精挑细选的热门 AI 工具</p>
            </div>
          </div>
          <div class="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
            <article
              v-for="(item, idx) in featuredResources"
              :key="item.id"
              class="glass-card-featured card-shine group relative p-6 perspective-1000"
              :style="{ animationDelay: `${idx * 100}ms` }"
            >
              <div class="absolute inset-0 bg-gradient-to-br from-primary-500/5 via-transparent to-accent-cyan/5 opacity-0 transition-opacity duration-500 group-hover:opacity-100 pointer-events-none rounded-[1.25rem]"></div>
              <div class="relative">
                <div class="flex items-start justify-between gap-3 mb-4">
                  <span class="inline-flex items-center rounded-lg border border-primary-500/30 bg-primary-500/10 px-3 py-1.5 text-xs font-medium text-primary-300 backdrop-blur-sm">
                    {{ item.category }}
                  </span>
                  <span class="flex h-6 w-6 items-center justify-center rounded-lg featured-badge text-white">
                    <svg class="h-3.5 w-3.5" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                    </svg>
                  </span>
                </div>
                <h3 class="text-lg font-semibold text-zinc-100 transition-colors duration-300 group-hover:text-white">{{ item.title }}</h3>
                <p class="mt-3 line-clamp-3 text-sm leading-relaxed text-zinc-500 group-hover:text-zinc-400 transition-colors duration-300">{{ item.description }}</p>
                <div class="mt-4 flex flex-wrap gap-2">
                  <span
                    v-for="tag in item.tags"
                    :key="tag"
                    class="tag px-2.5 py-1 text-xs text-zinc-500 group-hover:text-zinc-400"
                  >
                    #{{ tag }}
                  </span>
                </div>
                <a
                  :href="item.url"
                  target="_blank"
                  rel="noreferrer"
                  class="mt-6 inline-flex items-center gap-2.5 rounded-xl btn-primary px-5 py-2.5 text-sm font-medium text-white"
                >
                  访问工具
                  <svg class="h-4 w-4 transition-transform duration-200 group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </a>
              </div>
            </article>
          </div>
        </section>

        <div class="section-divider mb-10"></div>

        <section class="mb-10">
          <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center gap-4">
              <div class="flex h-10 w-10 items-center justify-center rounded-xl glass-panel">
                <svg class="h-5 w-5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
              </div>
              <div>
                <h2 class="text-xl font-semibold text-zinc-100">全部工具</h2>
                <p class="text-xs text-zinc-500">共 {{ filteredResources.length }} 条结果</p>
              </div>
            </div>
          </div>

          <div v-if="filteredResources.length === 0" class="glass-panel p-16 text-center">
            <div class="mx-auto mb-5 flex h-14 w-14 items-center justify-center rounded-2xl glass-panel">
              <svg class="h-7 w-7 text-zinc-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <p class="text-base font-medium text-zinc-400">未找到匹配结果</p>
            <p class="mt-2 text-sm text-zinc-600">请尝试其他关键词或切换分类筛选</p>
          </div>

          <div v-else class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            <article
              v-for="(item, idx) in filteredResources"
              :key="item.id"
              class="glass-card card-shine group relative p-5"
              :style="{ animationDelay: `${idx * 40}ms` }"
            >
              <div class="relative">
                <div class="flex items-start justify-between gap-3 mb-3">
                  <h3 class="text-sm font-semibold text-zinc-200 transition-colors duration-200 group-hover:text-white group-hover:underline decoration-primary-400/50 underline-offset-2">{{ item.title }}</h3>
                  <span class="shrink-0 rounded-lg border border-white/[0.06] bg-white/[0.02] px-2.5 py-1 text-xs text-zinc-500">{{ item.category }}</span>
                </div>
                <p class="line-clamp-3 text-sm leading-relaxed text-zinc-500 group-hover:text-zinc-400 transition-colors duration-200">{{ item.description }}</p>
                <div class="mt-3 flex flex-wrap gap-2">
                  <span
                    v-for="tag in item.tags"
                    :key="tag"
                    class="tag px-2 py-0.5 text-xs text-zinc-600 group-hover:text-zinc-500"
                  >
                    {{ tag }}
                  </span>
                </div>
                <a
                  v-if="isValidUrl(item.url)"
                  :href="item.url"
                  target="_blank"
                  rel="noreferrer"
                  class="mt-4 inline-flex items-center gap-2 rounded-lg border border-white/[0.06] bg-white/[0.02] px-3.5 py-2 text-xs font-medium text-zinc-400 transition-all duration-200 hover:border-primary-500/30 hover:bg-primary-500/10 hover:text-primary-300 hover:shadow-glow-sm"
                >
                  <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                  前往
                </a>
                <span v-else class="mt-4 inline-flex items-center gap-2 rounded-lg border border-red-500/20 bg-red-500/5 px-3 py-1.5 text-xs font-medium text-red-400/70">
                  <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                  链接待修复
                </span>
              </div>
            </article>
          </div>
        </section>

        <footer class="mt-16 border-t border-white/[0.06] pt-10 pb-8 text-center">
          <div class="flex items-center justify-center gap-2 mb-3">
            <div class="h-px w-12 bg-gradient-to-r from-transparent to-white/10"></div>
            <span class="text-xs text-zinc-600">LeeHub · AI 工具导航</span>
            <div class="h-px w-12 bg-gradient-to-l from-transparent to-white/10"></div>
          </div>
          <p class="text-xs text-zinc-600">持续更新 · 精选收录优质 AI 工具</p>
        </footer>
      </main>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'

const resources = ref([])
const search = ref('')
const selectedCategory = ref('全部')

onMounted(async () => {
  try {
    const apiUrl = import.meta.env.VITE_API_URL || '/api/resources'
    const res = await fetch(apiUrl)
    if (!res.ok) {
      throw new Error(`请求失败: ${res.status}`)
    }
    const data = await res.json()
    resources.value = Array.isArray(data) ? data : []
  } catch (error) {
    console.error('加载资源失败:', error)
    resources.value = []
  }
})

const isValidUrl = (url) => {
  if (typeof url !== 'string') return false
  try {
    const parsed = new URL(url)
    return parsed.protocol === 'http:' || parsed.protocol === 'https:'
  } catch {
    return false
  }
}

const validResources = computed(() => resources.value.filter((item) => isValidUrl(item.url)))

const categories = computed(() => {
  const all = resources.value.map((item) => item.category).filter(Boolean)
  return [...new Set(all)]
})

const filteredResources = computed(() => {
  const keyword = search.value.trim().toLowerCase()
  return resources.value.filter((item) => {
    const matchCategory = selectedCategory.value === '全部' || item.category === selectedCategory.value
    if (!matchCategory) return false
    if (!keyword) return true
    const text = [item.title, item.description, ...(item.tags || [])].join(' ').toLowerCase()
    return text.includes(keyword)
  })
})

const featuredResources = computed(() => {
  return filteredResources.value.filter((item) => item.featured).slice(0, 6)
})

const resetFilters = () => {
  search.value = ''
  selectedCategory.value = '全部'
}

const chipClass = (active) => {
  return active
    ? 'chip chip-active rounded-lg px-3.5 py-2 text-xs font-medium text-white'
    : 'chip rounded-lg px-3.5 py-2 text-xs font-medium text-zinc-400 hover:text-zinc-200'
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
