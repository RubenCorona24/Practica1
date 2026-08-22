import { fireEvent, render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, test, vi } from "vitest";
import { HomePage } from "./HomePage";
import { MemoryRouter } from "react-router";
import { useHeroPaginated } from "@/heroes/hooks/useHeroPaginated";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { FavoriteHeroProvider } from "@/heroes/context/FavoriteHeroContext";
//crear mock del componente
vi.mock("@/heroes/hooks/useHeroPaginated")
const mockUsePaginatedHero = vi.mocked(useHeroPaginated)


mockUsePaginatedHero.mockReturnValue({
    data: {
        heroes: [],   // ← objeto con heroes, no array directo
        total: 0,
        pages: 0
    },
    isLoading: false,
    isError: false,
    isSuccess: true
} as unknown as ReturnType<typeof useHeroPaginated>)
const queryClient = new QueryClient()

const renderHomePage = (initialEntries: string[] = ['/']) => {
    return render(
        <MemoryRouter initialEntries={initialEntries}>
            <FavoriteHeroProvider>
                <QueryClientProvider client={queryClient}>

                    <HomePage />

                </QueryClientProvider>
            </FavoriteHeroProvider>
        </MemoryRouter>
    )
}

describe("HomePage", () => {
    beforeEach(() => {
        vi.clearAllMocks() //limpiar mocks antes de cada test
    })
    test("should render component correctly (default values)", () => {
        const { container } = renderHomePage()
        expect(container).toMatchSnapshot() //snapshot del componente
    })
    test("should call usePaginatedHero with default values", () => {
        renderHomePage()
        screen.debug()
        expect(mockUsePaginatedHero).toHaveBeenCalled()
        expect(mockUsePaginatedHero).toHaveBeenCalledWith("6", "1", "all",)
    })
    test("should call usePaginatedHero with custom query params", () => {
        renderHomePage(['/?page=2&limit=10&category=villains'])
        expect(mockUsePaginatedHero).toHaveBeenCalledWith("10", "2", "villains",)

    })
    test("should call usePaginatedHero with default page and same limit on tab clicked", () => {
        renderHomePage(['/?tab=favorites&page=2&limit=10'])
        const [, , , villainsTab] = screen.getAllByRole("tab")
        fireEvent.click(villainsTab) //evento click en villains tab
        expect(mockUsePaginatedHero).toHaveBeenCalledWith("10", "1", "villain")
        screen.debug(villainsTab)
    })
})