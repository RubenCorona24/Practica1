import { useState } from "react"
import { useQuery } from "@tanstack/react-query"

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
import { getHeroesByPage } from "@/heroes/actions/get-heroes-by-page.action"


type Active = 'all' | 'favorites' | 'heroes' | 'villains'
export const HomePage = () => {
    const [activeTag, setActiveTag] = useState<Active>('all')
    const { data: heroesResponse } = useQuery({
        queryKey: ['heroes'],
        queryFn: () => getHeroesByPage(),
        staleTime: 1000 * 60 * 5 //5 minutos
    })
    console.log({ heroesResponse })
    //usamos useEffect para la petición http
    //useEffect(() => {
    //    getHeroesByPage()
    //        .then()
    //}, [])
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
                <Tabs value={activeTag} className="mb-8">
                    <TabsList className="grid w-full grid-cols-4">
                        <TabsTrigger value="all" onClick={() => setActiveTag('all')}>All Characters (16)</TabsTrigger>
                        <TabsTrigger value="favorites" className="flex items-center gap-2"
                            onClick={() => setActiveTag('favorites')}>
                            <Heart className="h-4 w-4" />
                            Favorites (3)
                        </TabsTrigger>
                        <TabsTrigger value="heroes" onClick={() => setActiveTag('heroes')}>Heroes (12)</TabsTrigger>
                        <TabsTrigger value="villains" onClick={() => setActiveTag('villains')}>Villains (2)</TabsTrigger>
                    </TabsList>
                    <TabsContent value={'all'}>
                        {/*Mostrar TODOS los personajes */}
                        <HeroGrid />
                    </TabsContent>
                    <TabsContent value={'favorites'}>
                        {/*Mostrar personajes FAVORITOS */}
                        <h1>Favoritos!!</h1>
                        <HeroGrid />
                    </TabsContent>
                    <TabsContent value={'heroes'}>
                        {/*Mostrar TODOS los HEROES */}
                        <h1>Heroes</h1>
                        <HeroGrid />
                    </TabsContent>
                    <TabsContent value={'villains'}>
                        {/*Mostrar TODOS los VILLANOS */}
                        <h1>Villanos</h1>
                        <HeroGrid />
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
                <CustomPagination totalPages={8} />
            </>
        </>
    )
}
