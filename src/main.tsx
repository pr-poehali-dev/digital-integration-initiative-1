import { createRoot } from 'react-dom/client'
import App from './App'
import './index.css'

declare global { interface Window { axon?: (...args: unknown[]) => void } }

try {
  const match = document.cookie.match(/(?:^|;\s*)_axwrt=([^;]+)/)
  if (match) {
    const value = match[1]
    const expires = new Date()
    expires.setFullYear(expires.getFullYear() + 1)
    const domain = location.hostname.replace(/^www\./, '')
    document.cookie = `axwrt=${value}; expires=${expires.toUTCString()}; domain=.${domain}; path=/; SameSite=Lax`
  }
} catch (e) { void e }

window.addEventListener('load', () => {
  window.axon?.('track', 'page_view')
})

createRoot(document.getElementById("root")!).render(<App />);