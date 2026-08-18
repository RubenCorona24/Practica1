import { describe, expect, test } from "vitest";
import { heroAPI } from "./hero.api";

const BASE_URL = import.meta.env.VITE_API_URL
describe("HeroAPI", () => {
    test("should be configure pointing to the testing server", () => {
        expect(heroAPI).toBeDefined() //esperar que esté definido
        expect(heroAPI.defaults.baseURL).toBe(`${BASE_URL}/api/heroes`)
        expect(BASE_URL).toBe("http://localhost:3000")
        console.log(heroAPI.defaults.baseURL)
    })
})