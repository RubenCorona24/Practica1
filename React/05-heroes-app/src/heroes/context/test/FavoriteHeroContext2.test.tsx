import { fireEvent, render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, test, vi } from "vitest";
import { FavoriteHeroContext, FavoriteHeroProvider } from "../FavoriteHeroContext";
import { use } from "react";
import type { Hero } from "@/heroes/interfaces/hero.interface";

const mockHero = {
    id: '1',
    name: 'batman'
} as Hero

//create a global objects mock
const localStorageMock = {
    getItem: vi.fn(),
    setItem: vi.fn(),
    clear: vi.fn()
}
Object.defineProperty(window, "localStorage", {
    value: localStorageMock, //pasamos el localStorageMock
    writable: true,
    configurable: true
})

//create a component that uses the context
const TestComponent = () => {
    const { favoriteCount, favorites, isFavorite, toggleFavorite } = use(FavoriteHeroContext) //usamos use en vez de useContext
    return (
        <div>
            <div data-testid="favorite-count">{favoriteCount}</div>
            <div data-testid="favorite-list">
                {favorites.map(hero => (
                    <div key={hero.id} data-testid={`Hero-${hero.id}`}>{hero.name}</div>
                ))}
            </div>
            <button data-testid="toggle-favorite"
                onClick={() => toggleFavorite(mockHero)}>
                Toggle Favorite
            </button>
            <div data-testid="is-favorite">
                {isFavorite(mockHero).toString()}
            </div>
        </div>
    )
}

//Función render para envolver el FavoriteHeroProvider dentro del TestComponent
const renderContextTest = () => {
    return render(
        <FavoriteHeroProvider>
            <TestComponent />
        </FavoriteHeroProvider>
    )
}

describe("FavoriteHeroContext", () => {
    beforeEach(() => {
        vi.clearAllMocks() //clear the localStorage mock
    })
    test("should initialize with default values", () => {
        //renderizamos componente
        renderContextTest() //this component has our context
        //test --- counter should be initialized at 0
        expect(screen.getByTestId("favorite-count").textContent).toBe('0')
        //test -- favorite list´s length should be 0
        expect(screen.getByTestId("favorite-list").children.length).toBe(0)
        screen.debug()
    })
    test("should add hero to favorites when toggleFavorite is called", () => {
        //renderizamos componente
        renderContextTest()
        //take the button
        const button = screen.getByTestId("toggle-favorite")
        fireEvent.click(button) //dispatch onClick event
        //test the favorite count
        expect(screen.getByTestId("favorite-count").textContent).toBe('1')
        expect(screen.getByTestId("is-favorite").textContent).toBe('true')
        expect(screen.getByTestId('Hero-1').textContent).toBe("batman")
        expect(localStorageMock.setItem).toHaveBeenCalled()
        expect(localStorageMock.setItem).toHaveBeenCalledWith('favorites', '[{\"id\":\"1\",\"name\":\"batman\"}]')

    })
    test("should remove hero from favorites when toggleFavorite is called", () => {
        localStorageMock.getItem.mockReturnValue(JSON.stringify([mockHero]))
        //renderizamos componente
        renderContextTest()
        //take the button
        const button = screen.getByTestId("toggle-favorite")
        screen.debug()
        fireEvent.click(button)
        expect(screen.getByTestId("favorite-count").textContent).toBe('0')
        expect(screen.getByTestId("is-favorite").textContent).toBe("false")
        expect(screen.queryByTestId("Hero-1")).toBeNull() //should be undefined

        expect(localStorageMock.getItem).toHaveBeenCalled() //expect getItem has been called
        expect(localStorageMock.getItem).toHaveBeenCalledWith('favorites')

    })
})