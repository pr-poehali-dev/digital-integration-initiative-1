import { LinkBioPage } from "./pages/LinkBioPage"
import { TestPage } from "./pages/TestPage"

function App() {
  const path = window.location.pathname
  if (path === '/test') return <TestPage />
  return <LinkBioPage />
}

export default App
