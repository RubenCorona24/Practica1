import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, test, vi } from "vitest";
import SearchPage from "./SearchPage";
import { MemoryRouter } from "react-router";
import { FavoriteHeroProvider } from "@/heroes/context/FavoriteHeroContext";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { searchHeroesAction } from "@/heroes/actions/search-heroes.action";

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
        renderSearchPage()
        //test the action values
        expect(mockSearchHeroesAction).toHaveBeenCalledWith({
            "name": undefined,
            "strength": undefined,
        })
        screen.debug()
    })
    test("should render SearchPage with CustomJombotron", () => {
        renderSearchPage()
        const CustomBreadcrumbs = screen.getByTestId("custom-breadcrumbs")
        screen.debug(CustomBreadcrumbs)
        const HeroStats = screen.getByTestId("hero-stats")
        screen.debug(HeroStats)
        expect(CustomBreadcrumbs).toBeDefined()
        expect(HeroStats).toBeDefined()
    })
})