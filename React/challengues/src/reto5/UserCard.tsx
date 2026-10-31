
import { Button } from "../components/ui/button"
import { useNavigate } from 'react-router'

export interface Geo { lat: string; lng: string }
export interface Address { street: string; suite: string; city: string; zipcode: string; geo: Geo }
export interface Company { name: string; catchPhrase: string; bs: string }
export interface User {
    id: number; name: string; username: string; email: string;
    address: Address; phone: string; website: string; company: Company;
}

const initials = (n: string) => n.split(" ").map((w) => w[0]).slice(0, 2).join("").toUpperCase();

function Row({ label, value, href }: { label: string; value: string; href?: string }) {
    return (
        <div className="flex items-baseline justify-between gap-6 border-b border-border py-3.5">
            <dt className="shrink-0 font-mono text-[10px] uppercase tracking-[0.22em] text-muted-foreground">{label}</dt>
            <dd className="min-w-0 text-right break-all">
                {href ? (
                    <a href={href} className="text-sm text-foreground underline-offset-4 transition-colors hover:text-brand hover:underline">
                        {value}
                    </a>
                ) : (
                    <span className="text-sm text-foreground">{value}</span>
                )}
            </dd>
        </div>
    );
}
interface Props {
    user: User
}
export const UserCard = ({ user }: Props) => {
    const navigate = useNavigate()
    const { address: a, company: c } = user;
    const lat = Number(a.geo.lat);
    const lng = Number(a.geo.lng);

    return (
        <article className="relative mx-auto w-full max-w-2xl rounded-3xl border border-border bg-card p-7 text-card-foreground shadow-[0_28px_70px_-45px_color-mix(in_oklab,var(--foreground)_45%,transparent)] sm:p-10">
            <Button onClick={() => navigate("/")}>Página Principal</Button>
            <header className="flex items-center justify-between font-mono text-[10px] uppercase tracking-[0.22em] text-muted-foreground">
                <span>Perfil · Nº {String(user.id).padStart(4, "0")}</span>
                <span className="flex items-center gap-2">
                    <span className="h-1.5 w-1.5 rounded-full bg-brand" />
                    {a.city}
                </span>
            </header>

            <div className="mt-8 flex items-center gap-5">
                <div className="grid h-16 w-16 shrink-0 place-items-center rounded-2xl border border-border bg-muted font-display text-xl font-medium sm:h-20 sm:w-20 sm:text-2xl">
                    {initials(user.name)}
                </div>
                <div className="min-w-0">
                    <h1 className="truncate font-display text-3xl tracking-tight sm:text-4xl">{user.name}</h1>
                    <p className="mt-2 text-sm text-muted-foreground">@{user.username} · {a.zipcode}</p>
                </div>
            </div>

            <dl className="mt-8 border-t border-border">
                <Row label="Correo" value={user.email} href={`mailto:${user.email}`} />
                <Row label="Teléfono" value={user.phone} href={`tel:${user.phone}`} />
                <Row label="Sitio web" value={user.website} href={`https://${user.website}`} />
                <Row label="Domicilio" value={`${a.street}, ${a.suite}`} />
            </dl>

            <section className="mt-8 flex flex-wrap items-start justify-between gap-6 border-t border-border pt-6">
                <div className="min-w-0">
                    <p className="font-mono text-[10px] uppercase tracking-[0.22em] text-muted-foreground">Afiliación</p>
                    <h2 className="mt-2 font-display text-lg">{c.name}</h2>
                    <p className="mt-1 max-w-xs text-sm text-muted-foreground">{c.catchPhrase}</p>
                </div>
                <ul className="flex max-w-[14rem] flex-wrap justify-end gap-1.5">
                    {c.bs.split(" ").map((w) => (
                        <li key={w} className="rounded-full border border-border px-2.5 py-1 text-[11px] text-muted-foreground">{w}</li>
                    ))}
                </ul>
            </section>

            <footer className="mt-6 flex items-center justify-between gap-4 rounded-2xl bg-muted px-4 py-3">
                <span className="font-mono text-[10px] uppercase tracking-[0.22em] text-muted-foreground">Coordenadas</span>
                <span className="flex items-center gap-3">
                    <span className="relative h-2 w-2 rounded-full bg-brand">
                        <span className="absolute inset-0 animate-ping rounded-full bg-brand/40" />
                    </span>
                    <span className="font-mono text-xs tabular-nums text-foreground">
                        {lat.toFixed(4)}°, {lng.toFixed(4)}°
                    </span>
                </span>
            </footer>
        </article>
    );
}
