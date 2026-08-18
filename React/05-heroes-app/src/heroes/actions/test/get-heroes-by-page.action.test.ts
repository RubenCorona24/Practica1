import { beforeEach, describe, expect, test } from "vitest";
import { getHeroesByPage } from "../get-heroes-by-page.action";
import AxiosMockAdapter from 'axios-mock-adapter'
import { heroAPI } from "@/heroes/api/hero.api";

//creamos variable de entorno
const BASE_URL = import.meta.env.VITE_API_URL

describe("getHeroesByPage", () => {

    const heroesAPIMock = new AxiosMockAdapter(heroAPI)
    beforeEach(() => {
        heroesAPIMock.reset(); //limpiar la instancia de mock
    })
    test("should return default heroes", async () => {
        heroesAPIMock.onGet("/").reply(200, {
            total: 10,
            pages: 2,
            heroes: [
                {
                    image: '1.jpg'
                },
                {
                    image: '2.jpg'
                }
            ]
        })
        const result = await getHeroesByPage(1)
        expect(result).toStrictEqual({
            total: 10,
            pages: 2,
            heroes: [
                { image: `${BASE_URL}/images/1.jpg` },
                { image: `${BASE_URL}/images/2.jpg` }
            ]
        })
        console.log(result)
    }),
        test("should return the correct heroes when page is not a number", async () => {
            const responseObject = {
                total: 10,
                pages: 1,
                heroes: []
            }
            heroesAPIMock.onGet("/").reply(200, responseObject)
            heroesAPIMock.resetHistory(); //reseteamos el historial
            const res = await getHeroesByPage("abc" as unknown as number)
            const params = heroesAPIMock.history.get[0].params;
            expect(res).toStrictEqual({ total: 10, pages: 1, heroes: [] })
            expect(params).toStrictEqual({ limit: 6, offset: 0, category: 'all' }) //que sea igual al objeto
        }),
        test("should return the correct heroes when page is string number", async () => {
            const responseObject = {
                total: 10,
                pages: 1,
                heroes: []
            }
            heroesAPIMock.onGet("/").reply(200, responseObject)
            heroesAPIMock.resetHistory(); //reseteamos el historial
            await getHeroesByPage('5' as unknown as number);
            const params = heroesAPIMock.history.get[0].params
            expect(params).toStrictEqual({ limit: 6, offset: 24, category: 'all' })
            console.log(params)
        }),
        test("should call the api with correct params", async () => {
            const responseObject = {
                total: 10,
                pages: 1,
                heroes: []
            }
            heroesAPIMock.onGet("/").reply(200, responseObject)
            heroesAPIMock.resetHistory(); //reseteamos el historial
            await getHeroesByPage(2, 10, 'heroes');
            const params = heroesAPIMock.history.get[0].params
            expect(params).toStrictEqual({ limit: 10, offset: 10, category: 'heroes' })
            console.log(params)
        })
})