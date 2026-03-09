<template>
  <div class="min-h-screen bg-[#f4f1e8] text-[#1f2937]">
    <header class="border-b border-[#d9d2c3] bg-[#f8f5ed]">
      <div class="mx-auto max-w-7xl px-5 py-10 md:px-8">
        <p class="inline-flex items-center rounded-full border border-[#c5b79d] bg-[#f1e8d8] px-3 py-1 text-xs font-semibold tracking-wide text-[#7b5b2a]">
          AITools 中文版
        </p>
        <h1 class="mt-4 text-4xl font-black leading-tight md:text-5xl">
          找到你真正会用上的 AI 工具
        </h1>
        <p class="mt-4 max-w-2xl text-sm text-[#5b6472] md:text-base">
          参考 There&apos;s An AI For That 的目录结构，做成更适合中文用户的工具导航。已收录 {{ resources.length }} 个工具，支持关键词、分类与标签快速筛选。
        </p>

        <div class="mt-8 grid gap-3 md:grid-cols-3">
          <article class="rounded-2xl border border-[#d7cbb5] bg-[#fffaf0] p-4">
            <p class="text-xs text-[#7b5b2a]">今日精选</p>
            <p class="mt-1 text-xl font-bold">{{ featuredResources.length }} 个</p>
          </article>
          <article class="rounded-2xl border border-[#d7cbb5] bg-[#fffaf0] p-4">
            <p class="text-xs text-[#7b5b2a]">分类总数</p>
            <p class="mt-1 text-xl font-bold">{{ categories.length }} 个</p>
          </article>
          <article class="rounded-2xl border border-[#d7cbb5] bg-[#fffaf0] p-4">
            <p class="text-xs text-[#7b5b2a]">可用链接</p>
            <p class="mt-1 text-xl font-bold">{{ validResources.length }} 个</p>
          </article>
        </div>
      </div>
    </header>

    <main class="mx-auto max-w-7xl px-5 py-8 md:px-8">
      <section class="rounded-3xl border border-[#d9d2c3] bg-white p-5 shadow-sm">
        <div class="grid gap-4 lg:grid-cols-[1fr_auto] lg:items-center">
          <input
            v-model="search"
            type="text"
            placeholder="搜索工具名、描述、标签，如：代码、图片、API"
            class="w-full rounded-2xl border border-[#ddd3c1] bg-[#fcfaf6] px-4 py-3 text-sm outline-none transition focus:border-[#b38b47]"
          />
          <button
            type="button"
            class="rounded-2xl bg-[#1f2937] px-5 py-3 text-sm font-semibold text-white hover:bg-[#111827]"
            @click="resetFilters"
          >
            重置筛选
          </button>
        </div>

        <div class="mt-4 flex flex-wrap gap-2">
          <button
            type="button"
            :class="chipClass(selectedCategory === '全部')"
            @click="selectedCategory = '全部'"
          >
            全部
          </button>
          <button
            v-for="cat in categories"
            :key="cat"
            type="button"
            :class="chipClass(selectedCategory === cat)"
            @click="selectedCategory = cat"
          >
            {{ cat }}
          </button>
        </div>
      </section>

      <section v-if="featuredResources.length" class="mt-8">
        <div class="mb-4 flex items-center justify-between">
          <h2 class="text-2xl font-black">今日推荐</h2>
          <span class="text-sm text-[#6b7280]">优先展示标记为 featured 的工具</span>
        </div>
        <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          <article
            v-for="item in featuredResources"
            :key="item.id"
            class="rounded-2xl border border-[#d9d2c3] bg-[#fffdf8] p-5"
          >
            <p class="text-xs font-semibold text-[#8b5e34]">{{ item.category }}</p>
            <h3 class="mt-2 text-xl font-bold">{{ item.title }}</h3>
            <p class="mt-2 line-clamp-3 text-sm text-[#4b5563]">{{ item.description }}</p>
            <div class="mt-4 flex flex-wrap gap-2">
              <span
                v-for="tag in item.tags"
                :key="tag"
                class="rounded-full bg-[#efe6d7] px-2 py-1 text-xs text-[#7a5b2f]"
              >
                #{{ tag }}
              </span>
            </div>
            <a
              :href="item.url"
              target="_blank"
              rel="noreferrer"
              class="mt-5 inline-flex rounded-xl bg-[#0f766e] px-3 py-2 text-sm font-semibold text-white hover:bg-[#0d665f]"
            >
              立即访问
            </a>
          </article>
        </div>
      </section>

      <section class="mt-10">
        <div class="mb-4 flex items-center justify-between">
          <h2 class="text-2xl font-black">全部工具</h2>
          <span class="text-sm text-[#6b7280]">共 {{ filteredResources.length }} 条结果</span>
        </div>

        <div v-if="filteredResources.length === 0" class="rounded-2xl border border-dashed border-[#d6cbb6] bg-[#fffaf0] p-10 text-center text-[#6b7280]">
          没有匹配结果，试试更短的关键词。
        </div>

        <div v-else class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          <article
            v-for="item in filteredResources"
            :key="item.id"
            class="rounded-2xl border border-[#e4dccf] bg-white p-5 transition hover:-translate-y-0.5 hover:border-[#bca67f]"
          >
            <div class="flex items-start justify-between gap-3">
              <h3 class="text-lg font-bold">{{ item.title }}</h3>
              <span class="rounded-full bg-[#f3ebde] px-2 py-1 text-xs text-[#7b5b2a]">{{ item.category }}</span>
            </div>
            <p class="mt-2 line-clamp-3 text-sm text-[#4b5563]">{{ item.description }}</p>
            <div class="mt-4 flex flex-wrap gap-2">
              <span
                v-for="tag in item.tags"
                :key="tag"
                class="rounded-full border border-[#ddd3c4] px-2 py-1 text-xs text-[#6b7280]"
              >
                {{ tag }}
              </span>
            </div>
            <a
              v-if="isValidUrl(item.url)"
              :href="item.url"
              target="_blank"
              rel="noreferrer"
              class="mt-5 inline-flex rounded-xl border border-[#1f2937] px-3 py-2 text-sm font-semibold text-[#1f2937] hover:bg-[#1f2937] hover:text-white"
            >
              打开官网
            </a>
            <span v-else class="mt-5 inline-flex rounded-xl border border-[#e11d48] px-3 py-2 text-sm font-semibold text-[#e11d48]">
              链接待修复
            </span>
          </article>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'

const resources = ref([])
const search = ref('')
const selectedCategory = ref('全部')

onMounted(async () => {
  try {
    const res = await fetch('/api/resources')
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
    ? 'rounded-full bg-[#1f2937] px-3 py-1.5 text-sm font-semibold text-white'
    : 'rounded-full border border-[#ddd3c4] bg-[#fcfaf6] px-3 py-1.5 text-sm text-[#4b5563] hover:border-[#bca67f]'
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
