import { CustomJombotron } from '@/components/custom/CustomJombotron'
import { HeroStats } from '@/heroes/components/HeroStats'
import { SearchControls } from './ui/SearchControls'
import { CustomBreadcrumbs } from '@/components/custom/CustomBreadcrumbs'
import { useSearchParams } from 'react-router'
import { useQuery } from '@tanstack/react-query'
import { searchHeroesAction } from '@/heroes/actions/search-heroes.action'
import { HeroGrid } from '@/heroes/components/HeroGrid'

export const SearchPage = () => {
    const [searchParams] = useSearchParams();
    const name = searchParams.get("name") ?? undefined;
    const strength = searchParams.get("strength") ?? undefined;
    const { data = [] } = useQuery({
        queryKey: ['search', { name, strength }],
        queryFn: () => searchHeroesAction({ name, strength }),
        staleTime: 1000 * 60 * 5
    })
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

            <HeroGrid heroes={data} />
        </>
    )
}

export default SearchPage