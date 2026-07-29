import { CustomJombotron } from '@/components/custom/CustomJombotron'
import { HeroStats } from '@/heroes/components/HeroStats'
import { SearchControls } from './ui/SearchControls'
import { CustomBreadcrumbs } from '@/components/custom/CustomBreadcrumbs'

export const SearchPage = () => {
    return (
        <>
            <CustomJombotron title='Search Your Superhero' description='Discover and explore your favorite superheroes' />

            <CustomBreadcrumbs pageName='Buscador' breadcrumbs={[{ label: "Superheroe", to: '/' },
            { label: "Superheroe 2", to: "/" },
            { label: "Superheroe 3", to: '/' }
            ]} />
            {/* Stats Dashboard */}
            <HeroStats />
            {/*Filter and search*/}

            <SearchControls />
        </>
    )
}

export default SearchPage