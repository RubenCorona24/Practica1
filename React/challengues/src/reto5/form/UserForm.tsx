import { useForm, type SubmitHandler } from "react-hook-form" //formularios
import type { UserFormInformation } from "../interfaces/interface"
import { Input } from "../../components/ui/input"
import { Button } from "../../components/ui/button"
import { useNavigate } from "react-router-dom"

interface Props {
    defaultValues: Partial<UserFormInformation> | undefined
    onSubmit: SubmitHandler<UserFormInformation>
    isPending?: boolean
}

const inputClass =
    "h-11 rounded-xl border-border/60 bg-muted/40 px-4 transition-all duration-200 placeholder:text-muted-foreground/70 hover:border-border focus-visible:border-primary focus-visible:bg-background focus-visible:ring-4 focus-visible:ring-primary/10"

const labelClass = "text-xs font-medium uppercase tracking-wider text-muted-foreground"

export const UserForm = ({ defaultValues, onSubmit, isPending }: Props) => {
    const navigate = useNavigate()
    const { register,
        handleSubmit,
        formState: { errors }
    } = useForm<UserFormInformation>({ defaultValues })

    return (
        <form
            onSubmit={handleSubmit(onSubmit)}
            className="relative mx-auto w-full max-w-md overflow-hidden rounded-3xl border border-border/60 bg-card p-8 shadow-[0_20px_60px_-20px_rgb(0_0_0/0.25)]"
        >
            {/* Línea de acento superior */}
            <div className="absolute inset-x-0 top-0 h-1 bg-gradient-to-r from-primary/0 via-primary to-primary/0" />

            <div className="mb-8 space-y-1">
                <span className="inline-flex items-center gap-2 rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
                    <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-primary" />
                    Nuevo registro
                </span>
                <h2 className="pt-3 text-2xl font-semibold tracking-tight text-foreground">Agregar usuario</h2>
                <p className="text-sm text-muted-foreground">Completa los datos para crear el perfil.</p>
            </div>

            <div className="space-y-5">
                <div className="space-y-2">
                    <label htmlFor="name" className={labelClass}>Nombre completo</label>
                    <Input id="name" type="text" className={inputClass} aria-invalid={!!errors.name} {...register("name", {
                        required: "Nombre completo obligatorio"
                    })} placeholder="Nombre completo" />
                </div>
                <div className="space-y-2">
                    <label htmlFor="username" className={labelClass}>Usuario</label>
                    <Input id="username" type="text" className={inputClass} aria-invalid={!!errors.username} {...register("username", {
                        required: "Nombre de usuario obligatorio"
                    })} placeholder="Nombre de usuario" />
                </div>
                <div className="space-y-2">
                    <label htmlFor="email" className={labelClass}>Correo</label>
                    <Input id="email" type="email" className={inputClass} aria-invalid={!!errors.email} {...register("email", {
                        required: "Email obligatorio"
                    })} placeholder="Correo electrónico" />
                </div>

                {(errors.name || errors.username || errors.email) && (
                    <div className="space-y-1 rounded-xl border border-destructive/20 bg-destructive/5 px-4 py-3">
                        {errors.name && <p role="alert" className="text-destructive text-sm">{errors.name.message}</p>}
                        {errors.username && <p role="alert" className="text-destructive text-sm">{errors.username.message}</p>}
                        {errors.email && <p role="alert" className="text-destructive text-sm">{errors.email.message}</p>}
                    </div>
                )}

                <Button
                    type="submit"
                    disabled={isPending}
                    className="group mt-2 h-11 w-full rounded-xl text-sm font-medium shadow-lg shadow-primary/20 transition-all duration-200 hover:-translate-y-0.5 hover:shadow-xl hover:shadow-primary/30 active:translate-y-0 disabled:translate-y-0 disabled:opacity-60"
                >
                    {isPending ? (
                        <span className="flex items-center gap-2">
                            <span className="h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
                            Guardando...
                        </span>
                    ) : (
                        <span className="flex items-center gap-2">
                            Guardar
                            <span className="transition-transform duration-200 group-hover:translate-x-1">→</span>
                        </span>
                    )}
                </Button>

                <Button
                    type="button"
                    variant="ghost"
                    onClick={() => navigate("/")}
                    className="h-11 w-full rounded-xl text-sm font-medium text-muted-foreground transition-colors duration-200 hover:bg-muted/60 hover:text-foreground"
                >
                    Página Principal
                </Button>
            </div>
        </form>
    )
}