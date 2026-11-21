<script setup>
import { ref } from 'vue'

// Backend URL is baked in at build time; set VITE_API_URL for deployments
const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const data = ref(null)
const error = ref(null)
const loading = ref(false)

async function callBackend() {
  loading.value = true
  error.value = null
  try {
    const res = await fetch(`${apiUrl}/api/hello`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    data.value = await res.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main>
    <h1>deployment_fun</h1>
    <p>Backend: <code>{{ apiUrl }}</code></p>
    <button @click="callBackend" :disabled="loading">
      {{ loading ? 'Lade…' : 'Backend aufrufen' }}
    </button>
    <pre v-if="data">{{ data }}</pre>
    <p v-if="error" class="error">Fehler: {{ error }}</p>
  </main>
</template>

<style>
body { font-family: system-ui, sans-serif; max-width: 40rem; margin: 3rem auto; padding: 0 1rem; }
button { padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer; }
pre { background: #f4f4f4; padding: 1rem; border-radius: 4px; }
.error { color: #c00; }
</style>
