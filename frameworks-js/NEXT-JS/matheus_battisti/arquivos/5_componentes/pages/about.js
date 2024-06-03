import Navbar from '../components/Navbar'
import Link from 'next/link'

export default function About() { 
    return ( 
    <>
        <Navbar/>
        <h1>Página de About</h1>
        <Link href="/"> 
            <a>Ir para a Home</a> 
        </Link>
    </>
    )
}