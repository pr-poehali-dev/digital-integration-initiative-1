export function TestPage() {
  return (
    <main className="relative min-h-screen flex flex-col items-center justify-center px-6">
      <div className="fixed inset-0 z-0 bg-gradient-to-br from-slate-50 via-white to-slate-100" />
      <div className="relative z-10 flex flex-col items-center gap-6">
        <h1 className="text-4xl font-bold text-gray-800">тест</h1>
        <button
          onClick={() => history.back()}
          className="px-6 py-3 rounded-2xl text-gray-700 font-medium text-sm"
          style={{
            background: "rgba(255,255,255,0.6)",
            backdropFilter: "blur(20px)",
            border: "1px solid rgba(255,255,255,0.6)",
            boxShadow: "0 4px 16px rgba(0,0,0,0.06)",
          }}
        >
          ← Назад
        </button>
      </div>
    </main>
  )
}
