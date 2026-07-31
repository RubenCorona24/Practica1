
import {
    Filter,
    Heart,
} from "lucide-react"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { CustomJombotron } from "@/components/custom/CustomJombotron"
import { HeroStats } from "@/heroes/components/HeroStats"
import { HeroGrid } from "@/heroes/components/HeroGrid"

import { CustomPagination } from "@/components/custom/CustomPagination"
import { CustomBreadcrumbs } from "@/components/custom/CustomBreadcrumbs"
import { useHeroSummary } from "@/heroes/hooks/useHeroSummary"
import { useHeroPaginated } from "@/heroes/hooks/useHeroPaginated"
import { useHomePage } from "@/heroes/hooks/useHomePage"


export const HomePage = () => {
    const { page,
        limit,
        selectedTab, category, setSearchParams } = useHomePage()
    //const [activeTag, setActiveTag] = useState<Active>('all')
    const { data: heroesResponse } = useHeroPaginated(limit, page, category)

    const { data: summary } = useHeroSummary();
    console.log({ heroesResponse })
    return (
        <>
            <>
                {/* Header */}
                <CustomJombotron title="Superhero Universe" description="Discover and manage superheroes and villains" />
                <CustomBreadcrumbs pageName="Super heroes" breadcrumbs={[{ label: "Superheroe", to: '/' },
                { label: "Superheroe 2", to: "/" },
                { label: "Superheroe 3", to: '/' }
                ]} />
                {/* Stats Dashboard */}
                <HeroStats />





                {/* Tabs */}
                <Tabs value={selectedTab} className="mb-8">
                    <TabsList className="grid w-full grid-cols-4">
                        <TabsTrigger value="all" onClick={() => setSearchParams((prev) => {
                            prev.set('tab', 'all')
                            prev.set('category', 'all')
                            prev.set('page', '1') //reseteamos a la página 1
                            return prev;
                        })}>All Characters ({summary?.totalHeroes})</TabsTrigger>
                        <TabsTrigger value="favorites" className="flex items-center gap-2"
                            onClick={() => setSearchParams((prev) => {
                                prev.set('tab', 'favorites')
                                return prev;
                            })}>
                            <Heart className="h-4 w-4" />
                            Favorites ({3})
                        </TabsTrigger>
                        <TabsTrigger value="heroes" onClick={() => setSearchParams((prev) => {
                            prev.set('tab', 'heroes')
                            prev.set('category', 'hero')
                            prev.set('page', '1')
                            return prev;
                        })}>Heroes ({summary?.heroCount})</TabsTrigger>
                        <TabsTrigger value="villains" onClick={() => setSearchParams((prev) => {
                            prev.set('tab', 'villains')
                            prev.set('category', 'villain')
                            prev.set('page', '1')
                            return prev;
                        })}>Villains ({summary?.villainCount})</TabsTrigger>
                    </TabsList>
                    <TabsContent value={'all'}>
                        {/*Mostrar TODOS los personajes */}
                        <HeroGrid heroes={heroesResponse?.heroes ?? []} />
                    </TabsContent>
                    <TabsContent value={'favorites'}>
                        {/*Mostrar personajes FAVORITOS */}
                        <h1>Favoritos!!</h1>
                        <HeroGrid heroes={heroesResponse?.heroes ?? []} />
                    </TabsContent>
                    <TabsContent value={'heroes'}>
                        {/*Mostrar TODOS los HEROES */}
                        <h1>Heroes</h1>
                        <HeroGrid heroes={heroesResponse?.heroes.filter(hero => hero.category === "Hero") ?? []} />
                    </TabsContent>
                    <TabsContent value={'villains'}>
                        {/*Mostrar TODOS los VILLANOS */}
                        <h1>Villanos</h1>
                        <HeroGrid heroes={heroesResponse?.heroes.filter(hero => hero.category === "Villain") ?? []} />
                    </TabsContent>
                </Tabs>

                {/* Results info */}
                <div className="flex justify-between items-center mb-6">
                    <div className="flex items-center gap-4">
                        <p className="text-gray-600">Showing 6 of 16 characters</p>
                        <Badge variant="secondary" className="flex items-center gap-1">
                            <Filter className="h-3 w-3" />
                            Filtered
                        </Badge>
                    </div>
                </div>
                {/*Character Grid */}



                {/* Pagination */}
                <CustomPagination totalPages={heroesResponse?.pages ?? 1} />
            </>
        </>
    )
}
