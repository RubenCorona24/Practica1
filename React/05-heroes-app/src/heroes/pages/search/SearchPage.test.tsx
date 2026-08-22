import { render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, test, vi } from "vitest";
import SearchPage from "./SearchPage";
import { MemoryRouter } from "react-router";
import { FavoriteHeroProvider } from "@/heroes/context/FavoriteHeroContext";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { searchHeroesAction } from "@/heroes/actions/search-heroes.action";
import type { Hero } from "@/heroes/interfaces/hero.interface";

//mock del CustomJombotron


//mock del CustomBreadCrumbs
vi.mock("@/components/custom/CustomBreadcrumbs", () => ({
    CustomBreadcrumbs: () => <div data-testid="custom-breadcrumbs">CustomBreadcrumbs</div>
}))
//mock del SearchHeroesAction
vi.mock("@/heroes/actions/search-heroes.action")
const mockSearchHeroesAction = vi.mocked(searchHeroesAction)

//mock del HeroStats
vi.mock("@/heroes/components/HeroStats", () => ({
    HeroStats: () => <div data-testid="hero-stats">Hero Stats</div>
}))

//mock del searchcintrols
vi.mock("./ui/SearchControls", () => ({
    SearchControls: () => <div data-testid="search-controls">SearchControls </div>
}))

//mock del HeroGrid
vi.mock("@/heroes/components/HeroGrid", () => ({
    HeroGrid: ({ heroes }: { heroes: Hero[] }) => <div data-testid="hero-grid">
        {
            heroes.map(h => (
                <div key={h.id}>{h.name}</div>
            ))
        }
    </div>
}))
const queryClient = new QueryClient()

const renderSearchPage = (initialEntries: string[] = ['/']) => {
    return render(
        <MemoryRouter initialEntries={initialEntries}>
            <FavoriteHeroProvider>
                <QueryClientProvider client={queryClient}>

                    <SearchPage />

                </QueryClientProvider>
            </FavoriteHeroProvider>
        </MemoryRouter>
    )
}

describe("SearchPage", () => {
    beforeEach(() => {
        vi.clearAllMocks()
    })
    test("should render SearchPage with default values", () => {
        const { container } = renderSearchPage()
        //test the action values
        expect(mockSearchHeroesAction).toHaveBeenCalledWith({
            "name": undefined,
            "strength": undefined,
        })
        screen.debug()
        expect(container).toMatchSnapshot()
    })
    test("should render SearchPage with components", () => {
        renderSearchPage()
        const CustomBreadcrumbs = screen.getByTestId("custom-breadcrumbs")
        screen.debug(CustomBreadcrumbs)
        const HeroStats = screen.getByTestId("hero-stats")
        screen.debug(HeroStats)
        expect(CustomBreadcrumbs).toBeDefined()
        expect(HeroStats).toBeDefined()
        const SearchControls = screen.getByTestId("search-controls")
        expect(SearchControls).toBeDefined()
    })
    test("should call search action with name parameter", () => {
        const { container } = renderSearchPage(['/search?name=superman'])
        //test the action values
        expect(mockSearchHeroesAction).toHaveBeenCalledWith({
            "name": 'superman',
            "strength": undefined,
        })
        expect(container).toMatchSnapshot()
    })
    test("should call search action with strength parameter", () => {
        const { container } = renderSearchPage(['/search?strength=6'])
        //test the action values
        expect(mockSearchHeroesAction).toHaveBeenCalledWith({
            "name": undefined,
            "strength": '6',
        })
        expect(container).toMatchSnapshot()
    })
    test("should call search action with strength and name parameters", () => {
        const { container } = renderSearchPage(['/search?strength=6&name=superman'])
        //test the action values
        expect(mockSearchHeroesAction).toHaveBeenCalledWith({
            "name": 'superman',
            "strength": '6',
        })
        expect(container).toMatchSnapshot()
    })
    test("should render HeroGrid with search results", async () => {
        const mockHeroes = [
            { id: '1', name: 'Clark Kent' } as unknown as Hero,
            { id: '2', name: 'Bruce Wayne' } as unknown as Hero
        ]
        //hacemos un Resolved de nuestro mock action mandando los mockHeroes
        mockSearchHeroesAction.mockResolvedValue(mockHeroes)
        renderSearchPage()
        await waitFor(() => {
            expect(screen.getByText("Clark Kent")).toBeDefined()
            expect(screen.getByText("Bruce Wayne")).toBeDefined()
            screen.debug(screen.getByTestId("hero-grid"))
        })

    })
})