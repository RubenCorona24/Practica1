import { renderHook, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, test, vi } from "vitest";
import { useHeroPaginated } from "../useHeroPaginated";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import type { PropsWithChildren } from "react";
import { getHeroesByPage } from "@/heroes/actions/get-heroes-by-page.action";

vi.mock('@/heroes/actions/get-heroes-by-page.action', () => ({
    getHeroesByPage: vi.fn()
}))

const mockGetHeroesByPage = vi.mocked(getHeroesByPage)
//nos creamos un customProvider
//nos creamos un customProvider
const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } }
})

const tanStackCustomProvider = () => {
    return ({ children }: PropsWithChildren) => (
        <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
    )
}

describe("usePaginatedHero", () => {
    beforeEach(() => {
        vi.clearAllMocks()
        queryClient.clear();
    })
    test("should return the initial state (isLoading)", async () => { //suponer el estado inicial (isLoading)
        //renderizamos el customHook
        const { result } = renderHook(() => useHeroPaginated('1', '6'), {
            wrapper: tanStackCustomProvider()
        })

        expect(result.current.isError).toBe(false)
        expect(result.current.isLoading).toBe(true)
    })
    test("should return success data when API call succeeds", async () => {

        const mockHeroesData = {
            total: 20,
            pages: 4,
            heroes: []
        }
        mockGetHeroesByPage.mockResolvedValue(mockHeroesData) //le pasamos la data mockeada

        const { result } = renderHook(() => useHeroPaginated('1', '6'), {
            wrapper: tanStackCustomProvider()
        })
        await waitFor(() => {
            expect(result.current.isSuccess).toBe(true)
        })


        expect(result.current.status).toBe("success")
        expect(mockGetHeroesByPage).toHaveBeenCalled()
        expect(mockGetHeroesByPage).toHaveBeenCalledWith(6, 1, 'all')
    })
    test("should call getHeroesByPage with correct arguments", async () => {

        const mockHeroesData = {
            total: 20,
            pages: 4,
            heroes: []
        }
        mockGetHeroesByPage.mockResolvedValue(mockHeroesData) //le pasamos la data mockeada

        const { result } = renderHook(() => useHeroPaginated('1', '6', 'villain'), {
            wrapper: tanStackCustomProvider()
        })
        await waitFor(() => {
            expect(result.current.isSuccess).toBe(true)
        })


        expect(result.current.status).toBe("success")
        expect(mockGetHeroesByPage).toHaveBeenCalled()
        expect(mockGetHeroesByPage).toHaveBeenCalledWith(6, 1, 'villain')
    })
})  