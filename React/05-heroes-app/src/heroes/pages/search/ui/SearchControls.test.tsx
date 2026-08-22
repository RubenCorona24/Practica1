import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, test } from "vitest";
import { SearchControls } from "./SearchControls";
import { MemoryRouter } from "react-router";

if (typeof window.ResizeObserver === "undefined") {
    class ResizeObserver {
        observe() { }
        unobserve() { }
        disconnect() { }
    }
    window.ResizeObserver = ResizeObserver
}
const renderWithRouter = (initialEntries: string[] = ['/']) => {
    return render(
        <MemoryRouter initialEntries={initialEntries}>
            <SearchControls />
        </MemoryRouter>
    )
}

describe("SearchControls", () => {
    test("should render component with default values", () => {
        const { container } = renderWithRouter()
        expect(container).toMatchSnapshot()
    })
    test("should set input value when seach param name is set", () => {
        renderWithRouter(['/?name=batman'])
        //take the placeholder input
        const input = screen.getByPlaceholderText("Search heroes, villains, powers, teams...")
        screen.debug(input)
        expect(input.getAttribute("value")).toBe("batman")
    })
    test("should change params when input is changed and enter is pressed", () => {
        renderWithRouter(['/?name=batman'])
        //take the placeholder input
        const input = screen.getByPlaceholderText("Search heroes, villains, powers, teams...")
        //disparamos evento
        fireEvent.change(input, { target: { value: 'superman' } })
        fireEvent.keyDown(input, { key: 'Enter' })
        screen.debug(input)
        expect(input.getAttribute("value")).toBe("superman") //should change value
    })
    test("should change param strength when slider change", () => {
        renderWithRouter(['/?name=batman&active-accordion=advance-filters']);
        const slider = screen.getByRole("slider")
        screen.debug(slider)
        console.log(slider.getAttribute("aria-valuenow"))
    })
})