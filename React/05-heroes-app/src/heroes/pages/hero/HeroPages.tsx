import { CustomBreadcrumbs } from '@/components/custom/CustomBreadcrumbs'
import { useParams } from 'react-router'

export const HeroPages = () => {
    const { idSlug = '' } = useParams()
    console.log({ idSlug })
    return (
        <div>
            <h1>HeroPage</h1>
            <CustomBreadcrumbs pageName='Heroe' breadcrumbs={[{ label: "Superheroe", to: '/' },
            { label: "Superheroe 2", to: "/" },
            { label: "Superheroe 3", to: '/' }
            ]} />
        </div>
    )
}
