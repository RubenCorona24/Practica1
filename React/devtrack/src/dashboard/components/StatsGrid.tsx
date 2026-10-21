import type { Stat } from '@/interfaces/stats'


interface Props {
    stats: Stat[]
}
export const StatsGrid = ({ stats }: Props) => {
    return (
        <div className="stats">
            {stats.map(({ icon: Icon, ...s }) => (
                <div className="stat" key={s.label}>
                    <div className="stat-top">
                        <span>{s.label}</span>
                        <span className={`stat-icon ${s.tone}`}><Icon size={17} /></span>
                    </div>
                    <div className="stat-value">{s.value}</div>
                    <div className="stat-note">
                        <span className={s.tone === 'amber' ? 'warning' : 'positive'}>{s.change}</span>{' '}
                        <span>{s.note}</span>
                    </div>
                </div>
            ))}
        </div>
    )
}
