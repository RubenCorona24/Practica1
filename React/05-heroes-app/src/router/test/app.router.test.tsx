import { describe, expect, test, vi } from "vitest";
import { appRouter } from "../app.router";
import { render, screen } from "@testing-library/react";
import { createMemoryRouter, Outlet, RouterProvider, useParams } from "react-router";

vi.mock("@/heroes/pages/home/HomePage", () => ({
    HomePage: () => <div data-testid="home-page">Home Page</div>
}))

vi.mock("@/heroes/layouts/HeroesLayout", () => ({
    HeroesLayout: () => <div data-testid="heroes-layout">
        Layout
        <Outlet />
    </div>
}))

//mock de HeroPage
vi.mock("@/heroes/pages/hero/HeroPage", () => ({
    SuperheroProfile: () => {
        const { idSlug = '' } = useParams()
        return (
            <div data-testid="hero-page">
                HeroPage: {idSlug}
            </div>
        )
    }
}))

//mock del SearchPage : Lazy component
vi.mock("@/heroes/pages/search/SearchPage", () => ({
    default: () => <div data-testid="search-page"></div>
}))

describe("appRouter", () => {
    test("should be configured as expected", () => {
        console.log(appRouter.routes)
        //tomamos snapshot de nuestra ruta
        expect(appRouter.routes).toMatchSnapshot()
    })
    test("should render home page at root path", () => {
        //nos creamos un router memorizado
        const router = createMemoryRouter(appRouter.routes, {
            initialEntries: ["/"]
        })
        //renderizamos el routerProvider
        render(<RouterProvider router={router} />)
        expect(screen.getByTestId("home-page")).toBeDefined()
        screen.debug()
    })
    test("should render hero page at /heroes/:idSlug path", () => {
        //nos creamos un router memorizado
        const router = createMemoryRouter(appRouter.routes, {
            initialEntries: ["/heroes/superman"]
        })
        //renderizamos el routerProvider
        render(<RouterProvider router={router} />)
        screen.debug()
        expect(screen.getByTestId("hero-page").innerHTML).toBe("HeroPage: superman")
    })
    //this test should be async because is Lazy component
    test("should redirect to home page for unknown routes", () => {
        const router = createMemoryRouter(appRouter.routes, {
            initialEntries: ["/another-page"]
        }) //at the time of selecting an unknown page, it should redirect to home page  
        //renderizamos el routerProvider
        render(<RouterProvider router={router} />)
        screen.debug()
        expect(screen.getByTestId("home-page")).toBeDefined() //select testid div
    })
})