import { CustomJombotron } from '@/components/custom/CustomJombotron'
import { HeroStats } from '@/heroes/components/HeroStats'
import { SearchControls } from './ui/SearchControls'

export const SearchPage = () => {
    return (
        <>
            <CustomJombotron title='Search Your Superhero' description='Discover and explore your favorite superheroes' />
            {/* Stats Dashboard */}
            <HeroStats />
            {/*Filter and search*/}

            <SearchControls />
        </>
    )
}

export default SearchPage