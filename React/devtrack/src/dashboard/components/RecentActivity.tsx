import type { ActivityItem } from '@/interfaces/activity'
import { Activity } from 'lucide-react'

interface Props {
    activities: ActivityItem[]
}

export const RecentActivity = ({ activities }: Props) => {
    return (
        <section>
            <div className="section-title">
                <h2>Actividad reciente</h2>
                <Activity size={16} className="text-muted-foreground" />
            </div>
            <div className="activity-list">
                {activities.map((a, i) => (
                    <div className="activity-item" key={i}>
                        <span className={`avatar ${a.tone}`}>{a.name}</span>
                        <div>
                            <p>{a.text}</p>
                            <div className="task-project">{a.project}</div>
                            <time>{a.time}</time>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    )
}
