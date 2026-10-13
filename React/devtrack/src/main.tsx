import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { DevTrackApp } from './DevTrack.tsx'
import './index.css'


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <DevTrackApp />
  </StrictMode>,
)
