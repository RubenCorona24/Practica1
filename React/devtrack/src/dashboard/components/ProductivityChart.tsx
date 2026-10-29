import { useState } from "react"

interface Props {
    completed: number
}

const WEEKDAYS = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
const CHART_GRID_Y = [15, 50, 85, 120]

const DIALOG_TITLES = {
    task: 'Nueva tarea',
    notifications: 'Notificaciones',
    help: 'Centro de ayuda',
}

const CHART_THIS_WEEK = {
    line: 'M25 85 C60 85 75 106 112 103 S160 35 200 50 S240 90 288 68 S325 10 376 32 S430 76 464 63 S510 28 550 38',
    fill: 'M25 85 C60 85 75 106 112 103 S160 35 200 50 S240 90 288 68 S325 10 376 32 S430 76 464 63 S510 28 550 38 L550 120 L25 120Z',
}
const CHART_LAST_WEEK = {
    line: 'M25 105 Q100 55 112 80 T200 100 T288 80 T376 50 T464 90 T550 80',
    fill: 'M25 105 Q100 55 112 80 T200 100 T288 80 T376 50 T464 90 T550 80 L550 120 L25 120Z',
}

export const ProductivityChart = ({ completed }: Props) => {
    const [period, setPeriod] = useState('Esta semana')
    const isThisWeek = period === 'Esta semana'
    const chartPaths = isThisWeek ? CHART_THIS_WEEK : CHART_LAST_WEEK
    return (
        <div className="activity-chart">
            <div className="section-title">
                <h2>Tu productividad</h2>
                <select
                    aria-label="Periodo de productividad"
                    className="text-[11px] bg-transparent text-muted-foreground outline-none"
                    value={period}
                    onChange={e => setPeriod(e.target.value)}
                >
                    <option>Esta semana</option>
                    <option>Semana anterior</option>
                </select>
            </div>

            <div className="flex gap-4 items-center mb-3">
                <span className="text-[11px] text-muted-foreground flex items-center gap-1.5">
                    <span className="status-dot" />Tareas completadas
                </span>
                <span className="text-[11px] positive">
                    {isThisWeek ? 12 + completed : 9} en total
                </span>
            </div>

            <svg
                className="chart"
                viewBox="0 0 560 145"
                role="img"
                aria-label={`Gráfica de tareas completadas: ${period}`}
                preserveAspectRatio="none"
            >
                {CHART_GRID_Y.map((y, i) => (
                    <g key={y}>
                        <text x="0" y={y + 3} className="chart-label">{6 - i * 2}</text>
                        <line x1="25" x2="550" y1={y} y2={y} className="chart-grid" />
                    </g>
                ))}
                <path className="chart-fill" d={chartPaths.fill} />
                <path className="chart-line" d={chartPaths.line} />
                {WEEKDAYS.map((d, i) => (
                    <text
                        className="chart-label"
                        key={d}
                        x={25 + i * 87}
                        y="142"
                        textAnchor={i === 6 ? 'end' : 'start'}
                    >
                        {d}
                    </text>
                ))}
            </svg>
        </div>
    )
}
